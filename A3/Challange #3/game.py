import pygame as pg
import math
import random

from car import Car
from tire import Tire
from barricade import Barricade


class Game:
    def __init__(self, width, height, title):
        # PyGame initialization
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)

        # Game variables
        self.soft_tires = Tire("SOFT", 10000.0, 12.5, -3.0, 0.05, -0.1, -0.02, 2.0)
        self.medium_tires = Tire("MEDIUM", 15000.0, 10, -2.0, 0.035, -0.08, -0.04, 1.75)
        self.hard_tires = Tire("HARD", 20000.0, 7.5, -1.0, 0.02, -0.06, -0.06, 1.5)
        self.destroyed_tires = Tire("DESTROYED", 0.0, 2.0, -0.2, 0.005, -0.1, -0.05, 0.5)

        self.lap_count = 15
        self.cpu_speed = 3.0
        self.car_skins = ("car_alfa.png", "car_aston.png", "car_bull.png", "car_mclaren.png", "car_merc.png")
        self.player = Car(pg.transform.scale(pg.image.load("res/textures/" + random.choice(self.car_skins)), (60, 21)).convert_alpha(), [500, 300], self.medium_tires)
        self.computer = Car(pg.transform.scale(pg.image.load("res/textures/" + random.choice(self.car_skins)), (60, 21)).convert_alpha(), [520, 340], self.medium_tires)
        self.computer.velocity = self.cpu_speed

        self.computer_path = ()
        self.randomize_path(0)
        self.computer_path_index = 0

        self.a_down = False
        self.d_down = False
        self.w_down = False
        self.s_down = False

        self.window_width = width
        self.window_height = height
        self.state_stack = []
        self.pit_timer: float = 0.0
        self.pit_timerange = (2.0, 5.0)  # Pit time range in seconds
        self.barricade_collision = False

        self.logo = pg.image.load("res/textures/logo.png")
        self.logo_small = pg.transform.scale(self.logo, [175, 175])

        self.font_200 = pg.font.Font("res/fonts/F1-regular.ttf", 200)
        self.font_100 = pg.font.Font("res/fonts/F1-regular.ttf", 100)
        self.font_50 = pg.font.Font("res/fonts/F1-regular.ttf", 50)
        self.font_40 = pg.font.Font("res/fonts/F1-regular.ttf", 40)
        self.font_30 = pg.font.Font("res/fonts/F1-regular.ttf", 30)
        self.font_24 = pg.font.Font("res/fonts/F1-regular.ttf", 25)
        self.font_12 = pg.font.Font("res/fonts/F1-regular.ttf", 12)

        self.bg_color = (157, 206, 226)
        self.color_black = (0, 0, 0)
        self.color_gray = (30, 30, 30)
        self.color_dark_grey = (67, 69, 74)
        self.color_red = (255, 0, 0)
        self.color_white = (255, 255, 255)
        self.color_green = (0, 136, 0)
        self.color_orange = (255, 140, 90)
        self.color_yellow = (255, 222, 89)
        self.color_yellowish_green = (201, 219, 0)

        self.title_text = self.font_100.render("acing", False, self.color_black).convert()
        self.credit_text = self.font_24.render("Game by Joshua (1092067) and Danny (1091749)", False, self.color_white).convert()

        self.click_sound = pg.mixer.Sound("res/sfx/click.wav")
        self.tire_change_sound = pg.mixer.Sound("res/sfx/tire-change.wav")
        self.tire_destroyed_sound = pg.mixer.Sound("res/sfx/tire-destroyed.wav")
        self.beep_sound = pg.mixer.Sound("res/sfx/beep.wav")

        self.clock = pg.time.Clock()
        self.fps = 60

    def randomize_path(self, random_range: int):
        self.computer_path = ((370 + random.randint(random_range * -1, random_range), 340 + random.randint(random_range * -1, random_range)),
                              (300 + random.randint(random_range * -1, random_range), 355 + random.randint(random_range * -1, random_range)),
                              (230 + random.randint(random_range * -1, random_range), 380 + random.randint(random_range * -1, random_range)),
                              (200 + random.randint(random_range * -1, random_range), 420 + random.randint(random_range * -1, random_range)),
                              (190 + random.randint(random_range * -1, random_range), 475 + random.randint(random_range * -1, random_range)),
                              (200 + random.randint(random_range * -1, random_range), 550 + random.randint(random_range * -1, random_range)),
                              (250 + random.randint(random_range * -1, random_range), 600 + random.randint(random_range * -1, random_range)),
                              (300 + random.randint(random_range * -1, random_range), 625 + random.randint(random_range * -1, random_range)),
                              (615 + random.randint(random_range * -1, random_range), 630 + random.randint(random_range * -1, random_range)),
                              (920 + random.randint(random_range * -1, random_range), 635 + random.randint(random_range * -1, random_range)),
                              (1010 + random.randint(random_range * -1, random_range), 610 + random.randint(random_range * -1, random_range)),
                              (1060 + random.randint(random_range * -1, random_range), 550 + random.randint(random_range * -1, random_range)),
                              (1050 + random.randint(random_range * -1, random_range), 420 + random.randint(random_range * -1, random_range)),
                              (1010 + random.randint(random_range * -1, random_range), 370 + random.randint(random_range * -1, random_range)),
                              (920 + random.randint(random_range * -1, random_range), 335 + random.randint(random_range * -1, random_range)),
                              (500 + random.randint(random_range * -1, random_range), 340 + random.randint(random_range * -1, random_range))
                              )

    def point_close_to_point(self, x1: float, y1: float, x2: float, y2: float, delta: float) -> bool:
        return abs(x1 - x2) <= delta and abs(y1 - y2) <= delta

    def player_can_pit(self) -> bool:
        # Debugging
        # print(f"{self.player.position[0]} {self.player.position[1]}")
        return 608 < self.player.position[0] < 640 and 188 < self.player.position[1] < 210 and self.player.velocity == 0.0

    def over_finish(self, entity) -> bool:
        # Finish line positions
        # map_finishline1 = pg.Rect((410, 280), (5, 120))
        # map_finishline2 = pg.Rect((445, 280), (5, 120))
        return 410 < entity.position[0] < 445 and 280 < entity.position[1] < 400 and entity.velocity > 0

    def points_reached(self, entity) -> bool:
        return entity.lapcount == 16

    def switch_player_tires(self, new_tires: Tire):
        self.player.tires = new_tires
        self.player.distance_driven = 0.0

    def reset_game(self):
        self.player = Car(pg.transform.scale(pg.image.load("res/textures/" + random.choice(self.car_skins)), (60, 21)).convert_alpha(),
                          [500, 300], self.medium_tires)
        self.computer = Car(pg.transform.scale(pg.image.load("res/textures/" + random.choice(self.car_skins)), (60, 21)).convert_alpha(),
                            [520, 340], self.medium_tires)
        self.a_down = False
        self.d_down = False
        self.w_down = False
        self.s_down = False
        self.pit_timer = 0.0
        self.barricade_collision = False
        self.computer_path_index = 0
        self.computer.velocity = self.cpu_speed

    def start(self):
        play_button = pg.Rect((265, 375), (750, 100))
        quit_button = pg.Rect((265, 500), (750, 100))

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(pg.mouse.get_pos()):
                        pg.quit()
                        exit(0)
                    elif play_button.collidepoint(pg.mouse.get_pos()):
                        # Go to main game loop
                        self.state_stack.append("GAME")
                        pg.mixer.Sound.play(self.click_sound)
                        self.game()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        exit(0)
                    else:  # Any key pressed except escape
                        # Go to main game loop
                        self.state_stack.append("GAME")
                        pg.mixer.Sound.play(self.click_sound)
                        self.game()

                # Render
                self.screen.fill(self.bg_color)

                # Grass background
                green_background = pg.Rect((0, 400), (self.screen.get_width(), 400))
                pg.draw.rect(self.screen, self.color_green, green_background)

                # Road
                road_background = pg.Rect((340, 400), (600, 400))
                pg.draw.rect(self.screen, self.color_black, road_background)
                # Road side - Left
                pg.draw.polygon(self.screen, self.color_black, ((340, 400), (340, 720), (250, 720)))
                # Road side - Right
                pg.draw.polygon(self.screen, self.color_black, ((940, 400), (940, 720), (1035, 720)))
                # Road side wall - left
                pg.draw.polygon(self.screen, self.color_red, ((340, 400), (250, 720), (210, 720), (300, 400)))
                # Road side wall - right
                pg.draw.polygon(self.screen, self.color_red, ((940, 400), (1035, 720), (1075, 720), (980, 400)))

                # Play button and text
                pg.draw.rect(self.screen, self.color_dark_grey, play_button, border_radius=15)
                if play_button.collidepoint(pg.mouse.get_pos()):
                    play_text = self.font_50.render("Play", False, self.color_red).convert()
                else:
                    play_text = self.font_50.render("Play", False, self.color_white).convert()
                self.screen.blit(play_text, play_text.get_rect(center=(play_button.centerx, play_button.centery)))
                # Quit button and text
                pg.draw.rect(self.screen, self.color_dark_grey, quit_button, border_radius=15)
                if quit_button.collidepoint(pg.mouse.get_pos()):
                    quit_text = self.font_50.render("Quit", False, self.color_red).convert()
                else:
                    quit_text = self.font_50.render("Quit", False, self.color_white).convert()
                self.screen.blit(quit_text, quit_text.get_rect(center=(quit_button.centerx, quit_button.centery)))
                # Logo
                self.screen.blit(self.logo_small, self.logo_small.get_rect(center=((self.window_width / 2) - 155, 92)))
                # Title text
                self.screen.blit(self.title_text, (540, 70))
                # Credit text
                self.screen.blit(self.credit_text, (300, 650))
                # PyGame Render
                pg.display.update()
                self.clock.tick(self.fps)

    def pause(self):
        paused_text = self.font_50.render("Paused", False, self.color_black).convert()
        return_button = pg.Rect((80, 500), (250, 100))
        quit_button = pg.Rect((1000, 500), (200, 100))

        while self.state_stack[-1] == "PAUSE":
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(pg.mouse.get_pos()):
                        pg.quit()
                        exit(0)
                    elif return_button.collidepoint(pg.mouse.get_pos()):
                        # Go back to previous state
                        self.state_stack.pop()
                        pg.mixer.Sound.play(self.click_sound)
                        break
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        # Go back to previous state
                        self.state_stack.pop()
                        pg.mixer.Sound.play(self.click_sound)
                        break

            # Update

            # Render
            self.screen.fill(self.bg_color)

            # Grass background
            green_background = pg.Rect((0, 400), (self.screen.get_width(), 400))
            pg.draw.rect(self.screen, self.color_green, green_background)

            # Road
            road_background = pg.Rect((340, 400), (600, 400))
            pg.draw.rect(self.screen, self.color_black, road_background)
            # Road side - Left
            pg.draw.polygon(self.screen, self.color_black, ((340, 400), (340, 720), (250, 720)))
            # Road side - Right
            pg.draw.polygon(self.screen, self.color_black, ((940, 400), (940, 720), (1035, 720)))
            # Road side wall - left
            pg.draw.polygon(self.screen, self.color_red, ((340, 400), (250, 720), (210, 720), (300, 400)))
            # Road side wall - right
            pg.draw.polygon(self.screen, self.color_red, ((940, 400), (1035, 720), (1075, 720), (980, 400)))

            # Paused text
            self.screen.blit(paused_text, paused_text.get_rect(center=(self.window_width / 2, 200)))
            # Return button
            pg.draw.rect(self.screen, self.color_dark_grey, return_button, border_radius=15)
            if return_button.collidepoint(pg.mouse.get_pos()):
                return_text = self.font_50.render("Return", False, self.color_red).convert()
            else:
                return_text = self.font_50.render("Return", False, self.color_white).convert()
            self.screen.blit(return_text,
                             return_text.get_rect(center=(return_button.centerx, return_button.centery)))
            # Quit button
            pg.draw.rect(self.screen, self.color_dark_grey, quit_button, border_radius=15)
            if quit_button.collidepoint(pg.mouse.get_pos()):
                quit_text = self.font_50.render("Quit", False, self.color_red).convert()
            else:
                quit_text = self.font_50.render("Quit", False, self.color_white).convert()
            self.screen.blit(quit_text, quit_text.get_rect(center=(quit_button.centerx, quit_button.centery)))

            # Logo
            self.screen.blit(self.logo_small, self.logo_small.get_rect(center=((self.window_width / 2) - 155, 92)))
            # Title text
            self.screen.blit(self.title_text, (540, 70))
            # PyGame Render
            pg.display.update()
            self.clock.tick(self.fps)

    def end_screen(self, victor):
        play_again_button = pg.Rect((265, 375), (750, 100))
        quit_button = pg.Rect((265, 500), (750, 100))

        while self.state_stack[-1] == "END":
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        exit(0)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(pg.mouse.get_pos()):
                        pg.quit()
                        exit(0)
                    elif play_again_button.collidepoint(pg.mouse.get_pos()):
                        self.reset_game()
                        self.state_stack.pop()
                        self.game()

            # Render
            self.screen.fill(self.bg_color)

            # Grass background
            green_background = pg.Rect((0, 400), (self.screen.get_width(), 400))
            pg.draw.rect(self.screen, self.color_green, green_background)

            # Road
            road_background = pg.Rect((340, 400), (600, 400))
            pg.draw.rect(self.screen, self.color_black, road_background)
            # Road side - Left
            pg.draw.polygon(self.screen, self.color_black, ((340, 400), (340, 720), (250, 720)))
            # Road side - Right
            pg.draw.polygon(self.screen, self.color_black, ((940, 400), (940, 720), (1035, 720)))
            # Road side wall - left
            pg.draw.polygon(self.screen, self.color_red, ((340, 400), (250, 720), (210, 720), (300, 400)))
            # Road side wall - right
            pg.draw.polygon(self.screen, self.color_red, ((940, 400), (1035, 720), (1075, 720), (980, 400)))

            # Play button and text
            pg.draw.rect(self.screen, self.color_dark_grey, play_again_button, border_radius=15)
            if play_again_button.collidepoint(pg.mouse.get_pos()):
                play_text = self.font_50.render("Play again", False, self.color_red).convert()
            else:
                play_text = self.font_50.render("Play again", False, self.color_white).convert()
            self.screen.blit(play_text, play_text.get_rect(center=(play_again_button.centerx, play_again_button.centery)))
            # Quit button and text
            pg.draw.rect(self.screen, self.color_dark_grey, quit_button, border_radius=15)
            if quit_button.collidepoint(pg.mouse.get_pos()):
                quit_text = self.font_50.render("Quit", False, self.color_red).convert()
            else:
                quit_text = self.font_50.render("Quit", False, self.color_white).convert()
            self.screen.blit(quit_text, quit_text.get_rect(center=(quit_button.centerx, quit_button.centery)))
            # Logo
            self.screen.blit(self.logo_small, self.logo_small.get_rect(center=((self.window_width / 2) - 155, 92)))
            # Title text
            self.screen.blit(self.title_text, (540, 70))
            # Winner text
            victor_text = self.font_50.render("And the winner is...", False, self.color_black).convert()
            self.screen.blit(victor_text, (380, 200))
            if victor == "Player":
                victor_result_text = self.font_100.render("The Player", False, self.color_red).convert()
                self.screen.blit(victor_result_text, (340, 260))
            else:
                victor_result_text = self.font_100.render("The Computer", False, self.color_red).convert()
                self.screen.blit(victor_result_text, (230, 260))
            # Credit text
            self.screen.blit(self.credit_text, (300, 650))
            # PyGame Render
            pg.display.update()
            self.clock.tick(self.fps)

    def game(self):
        ui_tire_health_20 = pg.Rect((15, 45), (40, 60))
        ui_tire_health_40 = pg.Rect((60, 45), (40, 60))
        ui_tire_health_60 = pg.Rect((105, 45), (40, 60))
        ui_tire_health_80 = pg.Rect((150, 45), (40, 60))
        ui_tire_health_100 = pg.Rect((195, 45), (40, 60))
        
        ui_current_tire_health_bg = pg.Rect((10, 40), (230, 70))
        ui_current_tire_bg = pg.Rect((250, 40), (230, 70))
        ui_current_speed_bg = pg.Rect((490, 40), (230, 70))
        ui_current_lap_player_bg = pg.Rect((1025, 40), (115, 70))
        ui_current_lap_computer_bg = pg.Rect((1145, 40), (115, 70))

        ui_current_tire_health_text = self.font_24.render("Tire Health", False, self.color_white).convert()
        ui_current_tire_text = self.font_24.render("Current Tire", False, self.color_white).convert()
        ui_current_speed_text = self.font_24.render("Speed (km/h)", False, self.color_white).convert()
        ui_current_lap_player_text = self.font_24.render("Player", False, self.color_white).convert()
        ui_current_lap_computer_text = self.font_24.render("PC", False, self.color_red).convert()

        ui_tire_swap_hint = self.font_30.render("[1] Soft, [2] Medium, [3] Hard", False, self.color_white).convert()

        ui_tire_soft = pg.transform.scale(pg.image.load("res/textures/tire_soft.png"), (64, 64))
        ui_tire_medium = pg.transform.scale(pg.image.load("res/textures/tire_medium.png"), (64, 64))
        ui_tire_hard = pg.transform.scale(pg.image.load("res/textures/tire_hard.png"), (64, 64))

        ui_tire_soft_text = self.font_24.render("S", False, (255, 0, 0)).convert()
        ui_tire_medium_text = self.font_24.render("M", False, (221, 179, 0)).convert()
        ui_tire_hard_text = self.font_24.render("H", False, (255, 107, 0)).convert()

        map_barricades = [Barricade(pg.transform.scale(pg.image.load("res/textures/barricade.png"), (550, 10)).convert_alpha(), [630, 420]),
                          Barricade(pg.transform.scale(pg.image.load("res/textures/barricade.png"),(550, 10)).convert_alpha(), [630, 540]),
                          Barricade(pg.transform.scale(pg.image.load("res/textures/barricade.png"),(1230, 10)).convert_alpha(), [645, 140]),
                          Barricade(pg.transform.scale(pg.image.load("res/textures/barricade.png"),(1230, 10)).convert_alpha(), [645, 710]),
                          Barricade(pg.transform.scale(pg.image.load("res/textures/barricade_vertical.png"),(10, 550)).convert_alpha(), [35, 425]),
                          Barricade(pg.transform.scale(pg.image.load("res/textures/barricade_vertical.png"),(10, 550)).convert_alpha(), [1255, 425]),
                          Barricade(pg.transform.scale(pg.image.load("res/textures/barricade_vertical.png"),(10, 120)).convert_alpha(), [360, 485]),
                          Barricade(pg.transform.scale(pg.image.load("res/textures/barricade_vertical.png"),(10, 120)).convert_alpha(), [900, 485]),
                          Barricade(pg.transform.scale(pg.image.load("res/textures/barricade.png"),(420, 10)).convert_alpha(), [625, 260])
                          ]

        # Make the default lap count 0 for both the player and the computer
        player_lap_count = 0
        computer_lap_count = 0

        player_finish_detected = False
        computer_finish_detected = False

        while self.state_stack[-1] == "GAME":
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        # Show pause menu
                        self.state_stack.append("PAUSE")
                        self.pause()
                    elif event.key == pg.K_e:
                        pg.mixer.Sound.play(self.beep_sound)
                    elif event.key == pg.K_a:
                        self.a_down = True
                    elif event.key == pg.K_d:
                        self.d_down = True
                    elif event.key == pg.K_w:
                        self.w_down = True
                    elif event.key == pg.K_s:
                        self.s_down = True
                    elif event.key == pg.K_1 and self.pit_timer <= 0:
                        if self.player.can_pit:
                            pg.mixer.Sound.play(self.tire_change_sound)
                            self.pit_timer = random.uniform(self.pit_timerange[0], self.pit_timerange[1])
                            self.switch_player_tires(self.soft_tires)
                    elif event.key == pg.K_2 and self.pit_timer <= 0:
                        if self.player.can_pit:
                            pg.mixer.Sound.play(self.tire_change_sound)
                            self.pit_timer = random.uniform(self.pit_timerange[0], self.pit_timerange[1])
                            self.switch_player_tires(self.medium_tires)
                    elif event.key == pg.K_3 and self.pit_timer <= 0:
                        if self.player.can_pit:
                            pg.mixer.Sound.play(self.tire_change_sound)
                            self.pit_timer = random.uniform(self.pit_timerange[0], self.pit_timerange[1])
                            self.switch_player_tires(self.hard_tires)
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_a:
                        self.a_down = False
                    elif event.key == pg.K_d:
                        self.d_down = False
                    elif event.key == pg.K_w:
                        self.w_down = False
                    elif event.key == pg.K_s:
                        self.s_down = False

            # Update
            if player_lap_count > self.lap_count:
                self.state_stack.append("END")
                self.end_screen("Player")
            elif computer_lap_count > self.lap_count:
                self.state_stack.append("END")
                self.end_screen("Computer")
            if not self.point_close_to_point(self.computer.position[0], self.computer.position[1], self.computer_path[self.computer_path_index][0], self.computer_path[self.computer_path_index][1], 5):
                angle = math.degrees(math.atan2(self.computer_path[self.computer_path_index][1] - self.computer.position[1], self.computer.position[0] - self.computer_path[self.computer_path_index][0]))
                if angle < 0:  # Angle is in range 0 - 180, so convert it to 0 - 360
                    angle += 360
                self.computer.rotation = angle

                self.computer.position[0] -= self.computer.velocity * math.cos(self.computer.rotation / 180 * math.pi)
                self.computer.position[1] += self.computer.velocity * math.sin(self.computer.rotation / 180 * math.pi)
            else:
                self.randomize_path(5)
                self.computer_path_index = (self.computer_path_index + 1) % len(self.computer_path)

            if self.pit_timer > 0.0:
                if self.pit_timer - 1 / self.fps < 0.0:
                    self.pit_timer = 0.0
                else:
                    self.pit_timer -= 1 / self.fps
            ui_pit_timer_text = self.font_24.render(f"Pit time: {self.pit_timer:.3f}", False, self.color_red).convert()

            # Player tires get destroyed when you drive more than they can take
            if self.player.distance_driven > self.player.tires.health and self.player.tires != self.destroyed_tires:
                pg.mixer.Sound.play(self.tire_destroyed_sound)
                self.player.tires = self.destroyed_tires

            if self.a_down and self.pit_timer <= 0 and not pg.sprite.collide_mask(self.player, self.computer) and not self.barricade_collision:
                if self.player.velocity != 0.0:  # Can only turn when moving forwards or backwards
                    self.player.rotation = (self.player.rotation + self.player.rotation_speed) % 360
            elif self.d_down and self.pit_timer <= 0 and not pg.sprite.collide_mask(self.player, self.computer) and not self.barricade_collision:
                if self.player.velocity != 0.0:  # Can only turn when moving forwards or backwards
                    if self.player.rotation - self.player.rotation_speed < 0:
                        self.player.rotation = 360.0 - self.player.rotation_speed
                    else:
                        self.player.rotation -= self.player.rotation_speed

            if self.w_down and self.pit_timer <= 0 and not pg.sprite.collide_mask(self.player, self.computer) and not self.barricade_collision:  # Accelerate forwards when W is held down
                self.player.acceleration = self.player.tires.max_forwards_acceleration
                self.player.velocity = min(self.player.velocity + self.player.acceleration, self.player.tires.max_forwards_velocity)
            elif self.s_down and self.pit_timer <= 0:  # Accelerate backwards when S is held down
                self.player.acceleration = self.player.tires.max_backwards_acceleration
                self.player.velocity = max(self.player.velocity + self.player.acceleration, self.player.tires.max_backwards_velocity)
            else:  # Slow down when neither W nor S are held down
                if -0.1 < self.player.velocity < 0.1:
                    self.player.acceleration = 0.0
                    self.player.velocity = 0.0
                elif self.player.velocity > 0.1:  # If player is moving forwards
                    self.player.acceleration = self.player.tires.drag
                else:  # If player is moving backwards
                    self.player.acceleration = self.player.tires.max_forwards_acceleration
                self.player.velocity = self.player.velocity + self.player.acceleration
            self.player.position[0] -= self.player.velocity * math.cos(self.player.rotation / 180 * math.pi)
            self.player.position[1] += self.player.velocity * math.sin(self.player.rotation / 180 * math.pi)

            # The player cannot turn at full capacity when not going fast, the turning speed is dependent on the velocity
            self.player.rotation_speed = min(self.player.velocity * 0.5, self.player.tires.max_rotation_speed)

            # Update the distance driven with the current tires
            self.player.distance_driven += abs(self.player.velocity)
            # Debugging
            # print(self.player.distance_driven)

            # Check if player can pit
            self.player.can_pit = self.player_can_pit()

            # Check if the player is over the finish
            self.player.over_finish = self.over_finish(self.player)
            self.computer.over_finish = self.over_finish(self.computer)

            if pg.sprite.collide_mask(self.player, self.computer):
                self.player.velocity = 0.0
                self.player.acceleration = 0.0

            for barricade in map_barricades:
                if pg.sprite.collide_rect(self.player, barricade):
                    self.player.velocity = 0.0
                    self.player.acceleration = 0.0
                    break
                self.barricade_collision = False

            # Render
            self.screen.fill(self.bg_color)

            # Game map
            # Grass
            map_grass = pg.Rect((0, 120), (self.screen.get_width(), 600))
            pg.draw.rect(self.screen, self.color_green, map_grass)
            # Road
            map_road = pg.Rect((300, 270), (660, 430))
            pg.draw.rect(self.screen, self.color_gray, map_road)
            pg.draw.circle(self.screen, self.color_gray, (300, 480), 220)
            pg.draw.circle(self.screen, self.color_gray, (960, 480), 220)
            # Finish line
            map_finishline1 = pg.Rect((410, 280), (5, 120))
            pg.draw.rect(self.screen, self.color_white, map_finishline1)
            map_finishtextbox = pg.Rect((415, 280), (30, 120))
            pg.draw.rect(self.screen, self.color_gray, map_finishtextbox)
            finishline_text = self.font_24.render("FINISH", False, self.color_white).convert()
            finishline_text = pg.transform.rotate(finishline_text, 90)
            self.screen.blit(finishline_text, finishline_text.get_rect(center=(map_finishtextbox.centerx, map_finishtextbox.centery)))
            map_finishline2 = pg.Rect((445, 280), (5, 120))
            pg.draw.rect(self.screen, self.color_white, map_finishline2)
            # Pit Lane
            map_pitlane = pg.Rect((400, 150), (450, 100))
            pg.draw.rect(self.screen, self.color_gray, map_pitlane)
            pg.draw.polygon(self.screen, self.color_gray, ((400, 150), (195, 300), (300, 400), (400, 250)))
            pg.draw.polygon(self.screen, self.color_gray, ((850, 150), (850, 250), (965, 400), (1065, 300)))
            # Pitstop location
            map_pitstop_white_bg = pg.Rect((575, 170), (100, 60))
            pg.draw.rect(self.screen, self.color_white, map_pitstop_white_bg)
            map_pitstop_grey_bg = pg.Rect((590, 170), (70, 80))
            pg.draw.rect(self.screen, self.color_gray, map_pitstop_grey_bg)
            map_pitstop_field = pg.Rect((585, 180), (80, 40))
            pg.draw.rect(self.screen, self.color_red, map_pitstop_field)
            pitstop_text = self.font_12.render("Pitstop", False, self.color_white).convert()
            self.screen.blit(pitstop_text, pitstop_text.get_rect(center=(map_pitstop_field.centerx, map_pitstop_field.centery)))
            # Center grass
            map_grass = pg.Rect((360, 410), (550, 140))
            pg.draw.rect(self.screen, self.color_green, map_grass)
            pg.draw.circle(self.screen, self.color_green, (360, 480), 70)
            pg.draw.circle(self.screen, self.color_green, (900, 480), 70)

            # Game UI Background
            ui_bg = pg.Rect((0, 0), (self.screen.get_width(), 120))
            pg.draw.rect(self.screen, self.color_dark_grey, ui_bg)
            # Game UI Splitter
            ui_splitter = pg.Rect((0, 120), (self.screen.get_width(), 10))
            pg.draw.rect(self.screen, self.color_gray, ui_splitter)

            # Game UI background for: Tire health, Current tire, Current Speed, Player current lap and Computer current lap
            pg.draw.rect(self.screen, self.color_black, ui_current_tire_health_bg)
            pg.draw.rect(self.screen, self.color_black, ui_current_tire_bg)
            pg.draw.rect(self.screen, self.color_black, ui_current_speed_bg)
            pg.draw.rect(self.screen, self.color_black, ui_current_lap_player_bg)
            pg.draw.rect(self.screen, self.color_black, ui_current_lap_computer_bg)

            # Game UI text for: Tire health, Current tire, Current Speed, Current position and Current tire
            self.screen.blit(ui_current_tire_health_text, (10, 10))
            self.screen.blit(ui_current_tire_text, (250, 10))
            self.screen.blit(ui_current_speed_text, (490, 10))
            self.screen.blit(ui_current_lap_player_text, (1025, 10))
            self.screen.blit(ui_current_lap_computer_text, (1145, 10))

            if self.player.tires.tire_type == "SOFT":
                self.screen.blit(ui_tire_soft, (335, 42))
                self.screen.blit(ui_tire_soft_text, (358, 61))
            elif self.player.tires.tire_type == "MEDIUM":
                self.screen.blit(ui_tire_medium, (335, 42))
                self.screen.blit(ui_tire_medium_text, (353, 60))
            elif self.player.tires.tire_type == "HARD":
                self.screen.blit(ui_tire_hard, (335, 42))
                self.screen.blit(ui_tire_hard_text, (356, 61))

            # Game UI: Tire Health (Health bars)
            if self.player.distance_driven < self.player.tires.health:
                pg.draw.rect(self.screen, self.color_red, ui_tire_health_20)
            if self.player.distance_driven < self.player.tires.health / 5 * 4:
                pg.draw.rect(self.screen, self.color_orange, ui_tire_health_40)
            if self.player.distance_driven < self.player.tires.health / 5 * 3:
                pg.draw.rect(self.screen, self.color_yellow, ui_tire_health_60)
            if self.player.distance_driven < self.player.tires.health / 5 * 2:
                pg.draw.rect(self.screen, self.color_yellowish_green, ui_tire_health_80)
            if self.player.distance_driven < self.player.tires.health / 5:
                pg.draw.rect(self.screen, self.color_green, ui_tire_health_100)

            # Show the tire swap hint
            if self.player.can_pit:
                self.screen.blit(ui_tire_swap_hint, (390, 460))

            # Pit timer text
            if self.pit_timer > 0.0:
                self.screen.blit(ui_pit_timer_text, (730, 10))

            # Finish - lap counter update
            # To detect if the player went over the finish and if so, add 1 to the lap count
            if self.player.over_finish:
                if not player_finish_detected:
                    player_lap_count += 1
                    player_finish_detected = True
            else:
                if player_finish_detected:
                    player_finish_detected = False
            # To detect if the computer went over the finish and if so, add 1 to the lap count
            if self.computer.over_finish:
                if not computer_finish_detected:
                    computer_lap_count += 1
                    computer_finish_detected = True
            else:
                if computer_finish_detected:
                    computer_finish_detected = False

            # Current player and Computer lap count
            # Player
            ui_current_lap_count_player_text = self.font_30.render(f"{player_lap_count}/{self.lap_count}", False, self.color_white).convert()
            self.screen.blit(ui_current_lap_count_player_text, (1035, 60))
            # Computer
            ui_current_lap_count_computer_text = self.font_30.render(f"{computer_lap_count}/{self.lap_count}", False, self.color_red).convert()
            self.screen.blit(ui_current_lap_count_computer_text, (1155, 60))

            # The actual speed display
            self.screen.blit(self.font_40.render(f"{int(self.player.velocity * 20)}", False, self.color_white).convert(), (500, 56))

            # Draw the car
            self.player.render(self.screen)
            self.computer.render(self.screen)
            # Debugging
            # print(f"{self.player_car.rotation} {math.cos(self.player_car.rotation / 180 * math.pi)}")
            # print(f"{self.player_car.rotation} {math.sin(self.player_car.rotation / 180 * math.pi)}")

            # Draw the barricades
            for barricade in map_barricades:
                barricade.render(self.screen)

            # This shows the computer path coordinates - Debugging
            # for coordinate in self.computer_path:
            #     pg.draw.rect(self.screen, self.color_red, pg.Rect(coordinate, (10, 10)))

            pg.display.update()
            self.clock.tick(self.fps)
