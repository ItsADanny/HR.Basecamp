# ---------------------------------------------------------------------------------------
# Project                      : SPACE RACE
# Project collaborators        : Sogaand, Julian, Danny
# Project objective            : Creating a digital board game based in the Terminal
# Project documentation        :
# Last change preformed (Date) : 06/03/2024 12:15
# Last change preformed by     : Julian
# Last change (Description)    : Created the needed trivia dictionary and Wordle list
# ---------------------------------------------------------------------------------------

trivia = [[">What is the largest planet in our solar system?\n>A: Jupiter, B: Earth, C: The Sun", "A"],
          [">Who was the first human to travel into space?\n>A: Yuri Gagarin, B: Neil Armstrong, C: Buzz Aldrin", "A"],
          [">Which planet is known as the 'Red Planet'?\n>A: Mars, B: Venus, C: Neptune", "A"],
          [">What is the farthest planet from the Sun in our solar system?\n>A: Neptune, B: Jupiter, C: Io", "A"],
          [">What is the name of the force that holds planets, moons, and other objects in orbit around a celestial body?\n>A: Gravity, B: Magic, C: Inertia", "A"],
          [">What is the name of the first artificial satellite launched into space by humans?\n>A: Sputnik 1, B: James Webb Telescope, C: Vanguard 1", "A"],
          [">Which planet has the Great Red Spot, a massive storm system larger than Earth?\n>A: Jupiter, B: Mars, C: Venus", "A"],
          [">What is the name of the spacecraft that successfully landed on Mars in 2012 and discovered evidence of past water activity?\n>A: Curiosity, B: Mars Reconnaissance Orbiter, C: Opportunity", "A"],
          [">What is the name of the spacecraft that visited Pluto in 2015, providing the first close-up images of the dwarf planet?\n>A: New Horizons, B: Voyager 1, C: Dawn", "A"],
          [">What is the name of the process where a star fuses hydrogen atoms to form helium, releasing energy in the form of light and heat?\n>A: Nuclear Fusion, B: Nuclear Fission, C: Ionization", "A"],
          [">What is the name of the region of space where the force of gravity is so strong that nothing, not even light, can escape?\n>A: Black Hole, B: Event Horizon, C: Your Mom", "A"],
          [">What is the name of the first woman to travel into space?\n>A: Valentina Tereshkova, B: Peggy Whitson, C: Gertrude Salma", "A"],
          [">What is the name of the process where a star runs out of fuel and collapses under its own gravity, resulting in a dense core known as a white dwarf?\n>A: Stellar Collapse, B: Black Hole, C: Neutron Star", "A"],
          [">What is the name of the nearest star to Earth, other than the Sun?\n>A: Barnard’s Star, B: Alpha Proxima, C: Wolf 359", "B"],
          [">What is the name of the phenomenon where light from a distant object is bent by the gravitational field of a massive object, such as a galaxy?\n>A: Black Hole, B: Gravitational Lensing, C: Supernova", "B"],
          [">What is the term for the point in an orbit around the Earth where a spacecraft is farthest from the planet?\n>A: Perigee, B: Apogee, C: Zenith", "B"],
          [">What is the name of the spacecraft that sent the first human-made object to reach interstellar space?\n>A: Sputnik 1, B: Voyager 1, C: New Horizons", "B"],
          [">What is the name of the phenomenon where a massive star collapses under its own gravity, resulting in a violent explosion?\n>A: Gamma Ray Burst, B: Supernova, C: Black Hole", "B"],
          [">What is the name of the largest moon in our solar system, which orbits Jupiter?\n>A: Titan, B: Ganymede, C: Io", "B"],
          [">What is the name of the phenomenon where a total solar eclipse occurs, creating a ring of light around the silhouette of the Moon?\n>A: Total Lunar Eclipse, B: Annual Eclipse, C: Total Solar Eclipse", "B"],
          [">What is the name of the telescope launched in 1990 that has provided invaluable insights into the universe's age, expansion rate, and composition?\n>A: James Webb Telescope, B: Hubble Space Telescope, C: Spitzer Space Telescope", "B"],
          [">What is the name of the spacecraft that carried astronauts to the International Space Station during NASA's Space Shuttle program?\n>A: Rosetta, B: Dawn, C: New Horizons", "B"],
          [">What is the name of the galaxy that contains our solar system?\n>A: Andromeda Galaxy, B: Sombrero Galaxy, C: Milky Way", "C"],
          [">What is the name of the spacecraft that carried the first humans to land on the Moon?\n>A: Voyager 11, B: Millenium Falcon, C: Apollo 11", "C"],
          [">Which planet has the largest volcano in the solar system, Olympus Mons?\n>A: Earth, B: Venus, C: Mars", "C"],
          [">What is the name of the telescope that orbits Earth and has provided stunning images of distant galaxies and nebulae?\n>A: James Webb Telescope, B: Spitzer Space Telescope, C: Hubble Space Telescope", "C"],
          [">What is the name of the theory that suggests the universe began as a hot, dense point and has been expanding and cooling ever since?\n>A: Geocentric Model, B: Steady State Model, C: Big Bang Theory", "C"],
          [">What is the name of the boundary where the Sun's solar wind meets the interstellar medium?\n>A: Oort Cloud, B: Heliosphere, C: Heliopause", "C"],
          [">What is the name of the spacecraft that successfully landed on Saturn's moon Titan in 2005 and sent back images of its surface?\n>A: Galileo, B: Kepler, C: Cassini-Huygens", "C"],
          [">Which planet has the most moons in our solar system?\n>A: Earth, B: Neptune, C: Jupiter", "C"]]

hangman = [["PLANET", "STAR", "ROCKET", "SPACE", "HORIZON"], # BEGINNER
          ["ORBIT", "GALAXY", "ALIEN", "COMET", "MOON"], # EASY
          ["ASTRONAUT", "EXOPLANET", "METEOR", "GRAVITY", "ECLIPSE"], # INTERMEDIATE
          ["BLACKHOLE", "TELESCOPE", "COSMOS", "INTERSTELLAR", "LIGHTYEAR"], # ADVANCED
          ["SUPERNOVA", "QUASAR", "UNIVERSE", "ASTEROID", "ASTEROID"]] # EXPERT