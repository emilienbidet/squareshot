class GameConfig:

    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 600

    COLOR_BLUE = (161, 237, 242)
    BAR_COLOR = (110,210,46)
    BAR_HEIGHT = 5

    PLAYER_IMAGE = ["media/player.png", "media/ia.png"]
    BULLET_IMAGE = ["media/bullet-player.png", "media/bullet-ia.png"]
    WALL_IMAGE = ["media/wall.png"]

    PLAYER_HEIGHT = 40
    PLAYER_WIDTH = PLAYER_HEIGHT

    PLAYER_STATE_MOVES = {"UP": -1,
                          "DOWN": 1,
                          "RIGHT": 1,
                          "LEFT": -1}

    WALL_HEIGHT = 50
    WALL_WIDTH = WALL_HEIGHT

    BULLET_HEIGHT = 20
    BULLET_WIDTH = BULLET_HEIGHT

    PLAYER_SPEED = 4
    BULLET_SPEED = 6
