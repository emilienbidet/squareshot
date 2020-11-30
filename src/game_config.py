class GameConfig:

    # Window configs

    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 800

    COLOR_BLUE = (161, 237, 242)
    TEXT_COLOR = (245,0,244)

    WALL_QUANTITY = 10 # percentage of walls to remove

    # ---------------------------------------------------

    # Wall configs

    WALL_HEIGHT = 50
    WALL_WIDTH = WALL_HEIGHT

    WALL_IMAGE = ["media/wall.png"]

    # ---------------------------------------------------

    # Player configs

    PLAYER_HEIGHT = 40
    PLAYER_WIDTH = PLAYER_HEIGHT

    PLAYER_IMAGE = ["media/player.png", "media/ia.png"]

    PLAYER_SPEED = 4

    PLAYER_MAX_HEALTH = 100
    PLAYER_MAX_STAMINA = 100

    BAR_HEALTH_COLOR = (110,210,46)
    BAR_STAMINA_COLOR = (70,145,255)
    BAR_NOTHING_COLOR = (191,191,191)
    BAR_HEIGHT = 5
    BAR_OFFSET = 6

    PLAYER_SPAWNS = [(WALL_WIDTH + 1, WALL_HEIGHT + 1),
                     (WINDOW_WIDTH - WALL_WIDTH - PLAYER_WIDTH - 1, WINDOW_HEIGHT - WALL_HEIGHT - PLAYER_HEIGHT - 1)]

    PLAYER_STATE_MOVES = {"UP": -1,
                          "DOWN": 1,
                          "RIGHT": 1,
                          "LEFT": -1}

    # ---------------------------------------------------

    # Bullet configs

    BULLET_HEIGHT = 20
    BULLET_WIDTH = BULLET_HEIGHT

    BULLET_IMAGE = ["media/bullet-player.png", "media/bullet-ia.png"]

    BULLET_SPEED = 6

    HEALTH_PER_BULLET = 10

    BULLET_COOLDOWN = 300 # ms
