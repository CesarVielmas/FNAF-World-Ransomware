import os
import random
import sys
import pygame
from PIL import Image
import ctypes

pygame.init()
pygame.font.init()
pygame.mixer.init()

info = pygame.display.Info()
width = info.current_w
height = info.current_h
#Functions
def draw_crt_lines(screen, width, height, line_thickness=4, gap=4):
    overlay = pygame.Surface((width, height), pygame.SRCALPHA)
    y = 0
    while y < height:
        pygame.draw.rect(overlay, (0, 0, 0, 90), (0, y, width, line_thickness))
        y += line_thickness + gap
    screen.blit(overlay, (0, 0))
def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#Variables Object
class GameInit:
    def __init__(self):
        self.isInitMusicWarning = False
        self.isInitWarning = False  
        self.isInitFadeInOutWarning = False  
        self.isInitGameTittle = False 
        self.isInitCompleteAnimations = False 
        self.isInitGameSelection = True
        self.isInitLoadWindow = True
        self.isInitDialogFreedbear = False
        self.isInitBackgroundAfterFreedbear = True
        self.isInitGameMap = True
        self.isInitCombat = True
        self.isInitShopBallonGirl = False
        self.isInitMiniGameBallonGirl = False
        self.isInitShopMangle = False
gameVariables = GameInit()
#Full Screen Game
icon = pygame.image.load(get_resource_path("assets/icon_game.ico"))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((height, width),pygame.FULLSCREEN)
pygame.display.set_caption("fnaworl")
font = pygame.font.SysFont("Arial", round(width * 0.05)) 
#Counter Game Init
start_time = pygame.time.get_ticks()  # Momento en que empieza
waitingTimeInitSound = 3000
waitingTimeInitWarning = 4000
waitingTimeInitFadeInOut = 7000
waitingTimeInitGame = 9000
waitingCompleteAnimationsInit = 12000
waitingScreenLoading = -1
waitingPassDialog = -1
waitingPassBackgroundFreddyAfterFreedbear = -1
#Assets Load Game
warningInit = pygame.image.load(get_resource_path("assets/warning_fnaf.png")).convert_alpha()
warningInit_rect = warningInit.get_rect(center=(width//2.2, height//2.5))

backgroundInitGame = pygame.image.load(get_resource_path("assets/background_init_game.png")).convert()
backgroundInitGame = pygame.transform.scale(backgroundInitGame, ((width * 0.95) - (width * 0.135), (height * 0.95) - (height * 0.135)))

imageAllAnimatronicsInit = pygame.image.load(get_resource_path("assets/image_all_animatronics.png")).convert_alpha()
imageAllAnimatronicsInit = pygame.transform.scale(imageAllAnimatronicsInit, (width * 0.85, height * 0.65))
imageAllAnimatronicsInit_rect = imageAllAnimatronicsInit.get_rect(center=(width//2.3, height//2))

imageTittleStartInit = pygame.image.load(get_resource_path("assets/tittle_game_init.png")).convert_alpha()
imageTittleStartInit = pygame.transform.scale(imageTittleStartInit, (width * 0.85, height * 0.75))
imageTittleStartInit_rect = imageTittleStartInit.get_rect(center=(width//2.45, height//2.4))

imageStartTittleInit = pygame.image.load(get_resource_path("assets/start_tittle_init.png")).convert_alpha()
imageStartTittleInit = pygame.transform.scale(imageStartTittleInit, (width * 0.26, height * 0.12))
imageStartTittleInit_rect = imageStartTittleInit.get_rect(center=(width//2.7, height//1.33))

imageTittleGameSelection = pygame.image.load(get_resource_path("assets/choose_your_character.png")).convert_alpha()
imageTittleGameSelection = pygame.transform.scale(imageTittleGameSelection, (width * 0.25, height * 0.15))
imageTittleGameSelection_rect = imageTittleGameSelection.get_rect(center=(width//5.5, height//9.5))

imageFreddyCharacter = pygame.image.load(get_resource_path("assets/freddy_icon.png")).convert_alpha()
imageFreddyCharacter = pygame.transform.scale(imageFreddyCharacter, (width * 0.1, height * 0.15))

backgroundLoadingScreen = pygame.image.load(get_resource_path("assets/loading_screen.png")).convert()
backgroundLoadingScreen = pygame.transform.scale(backgroundLoadingScreen, (width, height))

imageTittleLoadingScreen1 = pygame.image.load(get_resource_path("assets/chicken.png")).convert_alpha()
imageTittleLoadingScreen1 = pygame.transform.scale(imageTittleLoadingScreen1, (width * 0.25, height * 0.1))
imageTittleLoadingScreen1_rect = imageTittleLoadingScreen1.get_rect(center=(width//2.3, height//18))

imageFooterLoadingScreen1 = pygame.image.load(get_resource_path("assets/serbian_words_chicken.png")).convert_alpha()
imageFooterLoadingScreen1 = pygame.transform.scale(imageFooterLoadingScreen1, (width * 0.5, height * 0.1))
imageFooterLoadingScreen1_rect = imageFooterLoadingScreen1.get_rect(center=(width//2.3, height//1.26))

imageAnimatronicLoadingScreen1 = pygame.image.load(get_resource_path("assets/chicken_animatronic.png")).convert_alpha()
imageAnimatronicLoadingScreen1 = pygame.transform.scale(imageAnimatronicLoadingScreen1, (width * 0.2, height * 0.65))
imageAnimatronicLoadingScreen1_rect = imageAnimatronicLoadingScreen1.get_rect(center=(width//2.3, height//2.35))

backgroundFreedbear = pygame.image.load(get_resource_path("assets/freedbear_background.png")).convert()
backgroundFreedbear = pygame.transform.scale(backgroundFreedbear, (width, height))

imageFreddyStatic = pygame.image.load(get_resource_path("assets/freddy_static.png")).convert_alpha()
imageFreddyStatic = pygame.transform.scale(imageFreddyStatic, (width * 0.15, height * 0.44))
imageFreddyStatic_rect = imageFreddyStatic.get_rect(center=(width//1.4, height//1.65))

backgroundFreddyAfterFreedbear = pygame.image.load(get_resource_path("assets/background_freddy_after_freedbear.png")).convert_alpha()
backgroundFreddyAfterFreedbear = pygame.transform.scale(backgroundFreddyAfterFreedbear, (width, height))

backgroundMap = pygame.image.load(get_resource_path("assets/background_map_game.png")).convert()
backgroundMap = pygame.transform.scale(backgroundMap, (width, height))

backgroundBattle = pygame.image.load(get_resource_path("assets/background_battle_normal.png"))
backgroundBattle = pygame.transform.scale(backgroundBattle, (width, height))
#Sprites Freddy In Map
imageFreddyCharacterLeft = pygame.image.load(get_resource_path("assets/freddy_in_map_view_left.png")).convert_alpha()
imageFreddyCharacterLeft = pygame.transform.scale(imageFreddyCharacterLeft, (width * 0.06, height * 0.14))
imageFreddyCharacterLeft_rect = imageFreddyCharacterLeft.get_rect(center=(width // 1.32, height // 2.2))

imageFreddyCharacterRight = pygame.image.load(get_resource_path("assets/freddy_in_map_view_right.png")).convert_alpha()
imageFreddyCharacterRight = pygame.transform.scale(imageFreddyCharacterRight, (width * 0.06, height * 0.14))

imageFreddyCharacterTop = pygame.image.load(get_resource_path("assets/freddy_in_map_view_top.png")).convert_alpha()
imageFreddyCharacterTop = pygame.transform.scale(imageFreddyCharacterTop, (width * 0.06, height * 0.14))

imageFreddyCharacterBottom = pygame.image.load(get_resource_path("assets/freddy_in_map_view_bottom.png")).convert_alpha()
imageFreddyCharacterBottom = pygame.transform.scale(imageFreddyCharacterBottom, (width * 0.06, height * 0.14))

movement_freddy_x = 0
movement_freddy_y = 0
state_freddy_sprite = 1
state_battle_type = 0
waitingEnemyPosition = -1
start_animation_attacks = False
end_animation_attacks = False
audio_counter_sound_attacks_selection = 0
waitingAnimationAttacksStart = -1
waitingAnimationAttacksEnd = -1
waitingEnemyAttack = -1
waitingReapearAttacksFreddy = -1
attack_select_freddy = 0
animate_freddy_attack = False
animate_freddy_attack_waiting = -1
enter_to_attack_freddy = False
waitingEnterToAttackFreddy = -1
enemy_is_in_attack = False
on_punches_enemy = False
enemyIsInAttackWaiting = -1
onPunchesEnemyWaiting = -1
randomScenePunchEnemy = 0
waitingWiningBattle = -1
enterWinningBattle = False
waitingExitBattle = -1
waitingBackgroundBallonGirl = -1
movement_freedbear_mini_game_x = 0
movement_heart_mini_game_x = 0
type_movement_heart = 2
waitingWordsCompleteMiniGame = -1
movement_golden_freddy_map_x = 0
movement_golden_freddy_map_y = 0
waitingGhost = -1
waitingEnterFinalBattle = -1
#Sprites In Map
imageMangleInMap = pygame.image.load(get_resource_path("assets/mangle_in_map.png")).convert_alpha()
imageMangleInMap = pygame.transform.scale(imageMangleInMap,(width * 0.1,height * 0.18))
imageMangleInMap_rect = imageMangleInMap.get_rect(center=(width//1.7, height//8))

imageBonnieInMap = pygame.image.load(get_resource_path("assets/bonnie_in_map.png")).convert_alpha()
imageBonnieInMap = pygame.transform.scale(imageBonnieInMap,(width * 0.1,height * 0.18))
imageBonnieInMap_rect = imageBonnieInMap.get_rect(center=(width//15, height//7.5))

imageBlockInMap = pygame.image.load(get_resource_path("assets/block_in_map.png")).convert_alpha()
imageBlockInMap = pygame.transform.scale(imageBlockInMap,(width * 0.2,height * 0.22))
imageBlockInMap_rect = imageBlockInMap.get_rect(center=(width//4.55, height//3.4))

imageShadowInMap = pygame.image.load(get_resource_path("assets/shadow_in_map.png")).convert_alpha()
imageShadowInMap = pygame.transform.scale(imageShadowInMap,(width * 0.1,height * 0.17))
imageShadowInMap_rect = imageShadowInMap.get_rect(center=(width//2, height//1.33))

imageBallonGirlInMap = pygame.image.load(get_resource_path("assets/ballon_girl_in_map.png")).convert_alpha()
imageBallonGirlInMap = pygame.transform.scale(imageBallonGirlInMap,(width * 0.1,height * 0.18))
imageBallonGirlInMap_rect = imageBallonGirlInMap.get_rect(center=(width//1.27, height//1.35))

backgroundGameOver = pygame.image.load(get_resource_path("assets/background_game_over_screen.png")).convert()
backgroundGameOver = pygame.transform.scale(backgroundGameOver,(width,height))

backgroundMangleShop = pygame.image.load(get_resource_path("assets/background_mangle_shop.png")).convert()
backgroundMangleShop = pygame.transform.scale(backgroundMangleShop,(width,height))

imageMangleInShop = pygame.image.load(get_resource_path("assets/static_mangle_in_shop.png")).convert_alpha()
imageMangleInShop = pygame.transform.scale(imageMangleInShop,(width * 0.17,height * 0.5))
imageMangleInShop_rect = imageMangleInShop.get_rect(center=(width//7, height//1.75))

imageButtonBackShop = pygame.image.load(get_resource_path("assets/back_button_shops.png")).convert_alpha()
imageButtonBackShop = pygame.transform.scale(imageButtonBackShop,(width * 0.25,height * 0.15))
imageButtonBackShop_rect = imageButtonBackShop.get_rect(center=(width//1.41, height//1.315))

imageFreddyMask = pygame.image.load(get_resource_path("assets/freddy_mask_battle.png")).convert_alpha()
imageFreddyMask = pygame.transform.scale(imageFreddyMask,(width * 0.16,height * 0.23))
imageFreddyMask_rect = imageFreddyMask.get_rect(center=(width//2.3, height//4))

backgroundBallonGirlShop = pygame.image.load(get_resource_path("assets/background_ballon_girl_shop.png")).convert()
backgroundBallonGirlShop = pygame.transform.scale(backgroundBallonGirlShop,(width,height))

imageBallonGirlInShop = pygame.image.load(get_resource_path("assets/ballon_girl_in_shop.png")).convert_alpha()
imageBallonGirlInShop = pygame.transform.scale(imageBallonGirlInShop,(width * 0.15,height * 0.44))
imageBallonGirlInShop_rect = imageBallonGirlInShop.get_rect(center=(width//6.5, height//1.65))

imageButtonPlay = pygame.image.load(get_resource_path("assets/button_play_ballon_girl.png")).convert_alpha()
imageButtonPlay = pygame.transform.scale(imageButtonPlay,(width * 0.3,height * 0.25))
imageButtonPlay_rect = imageButtonPlay.get_rect(center=(width//2.45, height//3.6))

backgroundFoxyMap = pygame.image.load(get_resource_path("assets/background_foxy_map.png")).convert()
backgroundFoxyMap = pygame.transform.scale(backgroundFoxyMap,(width,height))

imageFoxyInMap = pygame.image.load(get_resource_path("assets/foxy_in_map.png")).convert_alpha()
imageFoxyInMap = pygame.transform.scale(imageFoxyInMap,(width * 0.1,height * 0.18))
imageFoxyInMap_rect = imageFoxyInMap.get_rect(center=(width//2, height//6))

imageSpriteGoldenFreddyInMap = pygame.image.load(get_resource_path("assets/freedbear_in_map.png")).convert_alpha()
imageSpriteGoldenFreddyInMap = pygame.transform.scale(imageSpriteGoldenFreddyInMap,(width * 0.06,height * 0.14))
imageSpriteGoldenFreddyInMap_rect = imageSpriteGoldenFreddyInMap.get_rect(center=(width//2, height//2))

imageGhostPart1 = pygame.image.load(get_resource_path("assets/ghost_in_map_part1.png")).convert_alpha()
imageGhostPart1 = pygame.transform.scale(imageGhostPart1,(width * 0.2,height * 0.25))

imageGhostPart2 = pygame.image.load(get_resource_path("assets/ghost_in_map_part2.png")).convert_alpha()
imageGhostPart2 = pygame.transform.scale(imageGhostPart2,(width * 0.4,height * 0.55))

background_winning_game = pygame.image.load(get_resource_path("assets/background_winning_game.png")).convert()
background_winning_game = pygame.transform.scale(background_winning_game,(width,height))

imageWinningWordsPart1 = pygame.image.load(get_resource_path("assets/words_winning_game_part1.png")).convert_alpha()
imageWinningWordsPart1 = pygame.transform.scale(imageWinningWordsPart1,(width * 0.3,height * 0.3))
imageWinningWordsPart1_rect = imageWinningWordsPart1.get_rect(center=(width//2.3, height//2.1))

imageWinningWordsPart2 = pygame.image.load(get_resource_path("assets/words_winning_game_part2.png")).convert_alpha()
imageWinningWordsPart2 = pygame.transform.scale(imageWinningWordsPart2,(width * 0.3,height * 0.3))
imageWinningWordsPart2_rect = imageWinningWordsPart2.get_rect(center=(width//2.3, height//2.1))

imageWinningFreedbear = pygame.image.load(get_resource_path("assets/freedbear_in_winning_game.png")).convert_alpha()
imageWinningFreedbear = pygame.transform.scale(imageWinningFreedbear,(width * 0.3,height * 0.25))
imageWinningFreedbear_rect = imageWinningFreedbear.get_rect(center=(width // 7, height//1.4))

background_winning_counter = pygame.image.load(get_resource_path("assets/background_final_counter_winning_game.png")).convert()
background_winning_counter = pygame.transform.scale(background_winning_counter,(width,height))

#Sprites In Battle
# Carga de recursos para ataques y minijuegos usando get_resource_path

imageAttackFreddySelection1 = pygame.image.load(get_resource_path("assets/attack_selection_1_battle.png")).convert_alpha()
imageAttackFreddySelection1 = pygame.transform.scale(imageAttackFreddySelection1, (width * 0.35, height * 0.12))
imageAttackFreddySelection1_rect = imageAttackFreddySelection1.get_rect(center=(width//2.08, height//2.2))

imageAttackFreddySelection2 = pygame.image.load(get_resource_path("assets/attack_selection_2_battle.png")).convert_alpha()
imageAttackFreddySelection2 = pygame.transform.scale(imageAttackFreddySelection2, (width * 0.35, height * 0.12))
imageAttackFreddySelection2_rect = imageAttackFreddySelection2.get_rect(center=(width//2.08, height//1.75))

imageAttackFreddySelection3 = pygame.image.load(get_resource_path("assets/attack_selection_3_battle.png")).convert_alpha()
imageAttackFreddySelection3 = pygame.transform.scale(imageAttackFreddySelection3, (width * 0.35, height * 0.12))
imageAttackFreddySelection3_rect = imageAttackFreddySelection3.get_rect(center=(width//2.08, height//1.45))

imageAttackEnemyNormal1 = pygame.image.load(get_resource_path("assets/attack_enemy_normal_1.png")).convert_alpha()
imageAttackEnemyNormal1 = pygame.transform.scale(imageAttackEnemyNormal1, (width * 0.2, height * 0.34))
imageAttackEnemyNormal1_rect = imageAttackEnemyNormal1.get_rect(center=(width//1.4, height//1.55))

imageAttackEnemyNormal2 = pygame.image.load(get_resource_path("assets/attack_enemy_normal_2.png")).convert_alpha()
imageAttackEnemyNormal2 = pygame.transform.scale(imageAttackEnemyNormal2, (width * 0.2, height * 0.4))
imageAttackEnemyNormal2_rect = imageAttackEnemyNormal2.get_rect(center=(width//1.4, height//1.6))

imageFreddyAttackFrame1 = pygame.image.load(get_resource_path("assets/freddy_in_attack_1_frame-removebg-preview.png")).convert_alpha()
imageFreddyAttackFrame1 = pygame.transform.scale(imageFreddyAttackFrame1, (width * 0.15, height * 0.44))
imageFreddyAttackFrame1_rect = imageFreddyAttackFrame1.get_rect(center=(width//1.4, height//1.65))

imageFreddyAttackFrame2 = pygame.image.load(get_resource_path("assets/freddy_in_attack_2_frame-removebg-preview.png")).convert_alpha()
imageFreddyAttackFrame2 = pygame.transform.scale(imageFreddyAttackFrame2, (width * 0.15, height * 0.44))
imageFreddyAttackFrame2_rect = imageFreddyAttackFrame2.get_rect(center=(width//1.4, height//1.65))

imageFreddyAttackFrame3 = pygame.image.load(get_resource_path("assets/freddy_in_attack_3_frame-removebg-preview.png")).convert_alpha()
imageFreddyAttackFrame3 = pygame.transform.scale(imageFreddyAttackFrame3, (width * 0.15, height * 0.44))
imageFreddyAttackFrame3_rect = imageFreddyAttackFrame3.get_rect(center=(width//1.4, height//1.65))

imageFreddyAttackFrame4 = pygame.image.load(get_resource_path("assets/freddy_in_attack_4_frame-removebg-preview.png")).convert_alpha()
imageFreddyAttackFrame4 = pygame.transform.scale(imageFreddyAttackFrame4, (width * 0.15, height * 0.44))
imageFreddyAttackFrame4_rect = imageFreddyAttackFrame4.get_rect(center=(width//1.4, height//1.65))

# Sprites de ataque de Freddy
imageFreddyAttackSprite1Part1 = pygame.image.load(get_resource_path("assets/attack_freddy_sprite_1_part1.png")).convert_alpha()
imageFreddyAttackSprite1Part1 = pygame.transform.scale(imageFreddyAttackSprite1Part1, (width * 0.06, height * 0.1))
imageFreddyAttackSprite1Part1_rect = imageFreddyAttackSprite1Part1.get_rect(center=(width//1.4, height//1.65))

imageFreddyAttackSprite1Part2 = pygame.image.load(get_resource_path("assets/attack_freddy_sprite_1_part2.png")).convert_alpha()
imageFreddyAttackSprite1Part2 = pygame.transform.scale(imageFreddyAttackSprite1Part2, (width * 0.06, height * 0.1))
imageFreddyAttackSprite1Part2_rect = imageFreddyAttackSprite1Part2.get_rect(center=(width//1.4, height//1.65))

imageFreddyAttackSprite1Part3 = pygame.image.load(get_resource_path("assets/attack_freddy_sprite_1_part3.png")).convert_alpha()
imageFreddyAttackSprite1Part3 = pygame.transform.scale(imageFreddyAttackSprite1Part3, (width * 0.06, height * 0.1))
imageFreddyAttackSprite1Part3_rect = imageFreddyAttackSprite1Part3.get_rect(center=(width//1.4, height//1.65))

imageFreddyAttackSprite2 = pygame.image.load(get_resource_path("assets/attack_freddy_sprite_2.png")).convert_alpha()
imageFreddyAttackSprite2 = pygame.transform.scale(imageFreddyAttackSprite2, (width * 0.3, height * 0.25))

imageFreddyAttackSprite3Part1 = pygame.image.load(get_resource_path("assets/attack_freddy_sprite_3_part1.png")).convert_alpha()
imageFreddyAttackSprite3Part1 = pygame.transform.scale(imageFreddyAttackSprite3Part1, (width * 0.13, height * 0.1))
imageFreddyAttackSprite3Part1_rect = imageFreddyAttackSprite3Part1.get_rect(center=(width//1.4, height//1.65))

imageFreddyAttackSprite3Part2 = pygame.image.load(get_resource_path("assets/attack_freddy_sprite_3_part2.png")).convert_alpha()
imageFreddyAttackSprite3Part2 = pygame.transform.scale(imageFreddyAttackSprite3Part2, (width * 0.13, height * 0.1))
imageFreddyAttackSprite3Part2_rect = imageFreddyAttackSprite3Part2.get_rect(center=(width//1.45, height//1.75))

imageFreddyAttackSprite3Part3 = pygame.image.load(get_resource_path("assets/attack_freddy_sprite_3_part3.png")).convert_alpha()
imageFreddyAttackSprite3Part3 = pygame.transform.scale(imageFreddyAttackSprite3Part3, (width * 0.13, height * 0.1))
imageFreddyAttackSprite3Part3_rect = imageFreddyAttackSprite3Part3.get_rect(center=(width//1.35, height//1.55))

imageFreddyAttackSprite3Part4 = pygame.image.load(get_resource_path("assets/attack_freddy_sprite_3_part4.png")).convert_alpha()
imageFreddyAttackSprite3Part4 = pygame.transform.scale(imageFreddyAttackSprite3Part4, (width * 0.13, height * 0.1))
imageFreddyAttackSprite3Part4_rect = imageFreddyAttackSprite3Part4.get_rect(center=(width//1.5, height//1.8))

imageFreddyAttackSprite3Part5 = pygame.image.load(get_resource_path("assets/attack_freddy_sprite_3_part5.png")).convert_alpha()
imageFreddyAttackSprite3Part5 = pygame.transform.scale(imageFreddyAttackSprite3Part5, (width * 0.13, height * 0.1))
imageFreddyAttackSprite3Part5_rect = imageFreddyAttackSprite3Part5.get_rect(center=(width//1.4, height//1.65))

# Fondos de punch enemigo
backgroundPunchEnemy1 = pygame.image.load(get_resource_path("assets/background_battle_punch_enemy_1.jpg")).convert_alpha()
backgroundPunchEnemy1 = pygame.transform.scale(backgroundPunchEnemy1, (width, height))
backgroundPunchEnemy2 = pygame.image.load(get_resource_path("assets/background_battle_punch_enemy_2.jpg")).convert_alpha()
backgroundPunchEnemy2 = pygame.transform.scale(backgroundPunchEnemy2, (width, height))
backgroundPunchEnemy3 = pygame.image.load(get_resource_path("assets/background_battle_punch_enemy_3.png")).convert_alpha()
backgroundPunchEnemy3 = pygame.transform.scale(backgroundPunchEnemy3, (width, height))

# Imágenes finales de batalla
imageDeadEnemyIsOn = pygame.image.load(get_resource_path("assets/enemy_is_dead_battle.png")).convert_alpha()
imageDeadEnemyIsOn = pygame.transform.scale(imageDeadEnemyIsOn, (width * 0.2, height * 0.25))
imageDeadEnemyIsOn_rect = imageDeadEnemyIsOn.get_rect(center=(width//6, height//1.8))

imageWinningBattle1 = pygame.image.load(get_resource_path("assets/winning_battle_1_phase.png")).convert_alpha()
imageWinningBattle1 = pygame.transform.scale(imageWinningBattle1, (width * 0.4, height * 0.55))
imageWinningBattle2 = pygame.image.load(get_resource_path("assets/winning_battle_2_phase.png")).convert_alpha()
imageWinningBattle2 = pygame.transform.scale(imageWinningBattle2, (width * 0.4, height * 0.55))
imageWinningBattle3 = pygame.image.load(get_resource_path("assets/winning_battle_3_phase.png")).convert_alpha()
imageWinningBattle3 = pygame.transform.scale(imageWinningBattle3, (width * 0.4, height * 0.55))

# Mini juego Ballon Girl
backgroundMiniGameBallonGirl = pygame.image.load(get_resource_path("assets/background_mini_game_ballon_girl.png")).convert()
backgroundMiniGameBallonGirl = pygame.transform.scale(backgroundMiniGameBallonGirl, (width, height))

imageFreedbearMiniGameBallonGirl = pygame.image.load(get_resource_path("assets/freedbear_mini_game_ballon_girl.png")).convert_alpha()
imageFreedbearMiniGameBallonGirl = pygame.transform.scale(imageFreedbearMiniGameBallonGirl, (width * 0.35, height * 0.25))
imageFreedbearMiniGameBallonGirl_rect = imageFreedbearMiniGameBallonGirl.get_rect(center=(width//1.5, height//7.5))

imageHeartMiniGameBallonGirl = pygame.image.load(get_resource_path("assets/heart_mini_game_ballon_girl.png")).convert_alpha()
imageHeartMiniGameBallonGirl = pygame.transform.scale(imageHeartMiniGameBallonGirl, (width * 0.1, height * 0.15))
imageHeartMiniGameBallonGirl_rect = imageHeartMiniGameBallonGirl.get_rect(center=(width//1.27, height//1.325))

imageWinningMiniGameBallonGirl = pygame.image.load(get_resource_path("assets/complete_mini_game_ballon_girl.png")).convert_alpha()
imageWinningMiniGameBallonGirl = pygame.transform.scale(imageWinningMiniGameBallonGirl, (width * 0.55, height * 0.35))
imageWinningMiniGameBallonGirl_rect = imageWinningMiniGameBallonGirl.get_rect(center=(width//2.3, height//2.1))

# Batalla contra Golden Freddy
imageGoldenFreddyBattle = pygame.image.load(get_resource_path("assets/final_boss_battle.png")).convert_alpha()
imageGoldenFreddyBattle = pygame.transform.scale(imageGoldenFreddyBattle, (width * 0.4, height * 0.55))
imageGoldenFreddyBattle_rect = imageGoldenFreddyBattle.get_rect(center=(width//5, height//1.95))

imageWordsGoldenFreddyBattle = pygame.image.load(get_resource_path("assets/final_battle_words.png")).convert_alpha()
imageWordsGoldenFreddyBattle = pygame.transform.scale(imageWordsGoldenFreddyBattle, (width * 0.6, height * 0.75))
imageWordsGoldenFreddyBattle_rect = imageWordsGoldenFreddyBattle.get_rect(center=(width//2, height//2.5))

attack_type = random.randint(1, 2)
#DiALOGS FREEDBEAR
dialog_freedbear1 = pygame.image.load(get_resource_path("assets/dialog_freedbear1.png")).convert()
dialog_freedbear1 = pygame.transform.scale(dialog_freedbear1, (width * 0.05, height * 0.04))

dialog_freedbear2 = pygame.image.load(get_resource_path("assets/dialog_freedbear2.png")).convert()
dialog_freedbear2 = pygame.transform.scale(dialog_freedbear2, (width * 0.3, height * 0.04))

dialog_freedbear3 = pygame.image.load(get_resource_path("assets/dialog_freedbear3.png")).convert()
dialog_freedbear3 = pygame.transform.scale(dialog_freedbear3, (width * 0.45, height * 0.04))

dialog_freedbear4 = pygame.image.load(get_resource_path("assets/dialog_freedbear4.png")).convert()
dialog_freedbear4 = pygame.transform.scale(dialog_freedbear4, (width * 0.45, height * 0.1))

dialog_freedbear5 = pygame.image.load(get_resource_path("assets/dialog_freedbear5.png")).convert()
dialog_freedbear5 = pygame.transform.scale(dialog_freedbear5, (width * 0.1, height * 0.04))

imageArrowPassDialogFreedbear = pygame.image.load(get_resource_path("assets/pass_dialog_arrow.png")).convert_alpha()
imageArrowPassDialogFreedbear = pygame.transform.scale(imageArrowPassDialogFreedbear, (width * 0.1, height * 0.1))

buttonStartDialogFreedbear = pygame.image.load(get_resource_path("assets/button_start_dialog_freedbear.png")).convert_alpha()
buttonStartDialogFreedbear = pygame.transform.scale(buttonStartDialogFreedbear, (width * 0.25, height * 0.15))

counterDialogFreedbear = 0
# GIFS LOAD
gifFreedBear = Image.open(get_resource_path("assets/freedbear_moveset.gif"))
framesFreedbear = []
durationsFreedbear = []

try:
    while True:
        frame = gifFreedBear.convert("RGBA")
        resized_frame = frame.resize((int(width * 0.15), int(height * 0.6)), Image.Resampling.LANCZOS)
        duration = gifFreedBear.info.get("duration", 10)  # duración por frame en ms
        pygame_frame = pygame.image.fromstring(resized_frame.tobytes(), resized_frame.size, resized_frame.mode)
        framesFreedbear.append(pygame_frame)
        durationsFreedbear.append(duration)
        gifFreedBear.seek(gifFreedBear.tell() + 1)
except EOFError:
    pass

frame_indexFreedbear = 0

gifEnemyNormal = Image.open(get_resource_path("assets/normal_enemy_battle.gif"))
framesEnemyNormal = []
durationsEnemyNormal = []

try:
    while True:
        frame = gifEnemyNormal.convert("RGBA")
        resized_frame = frame.resize((int(width * 0.21), int(height * 0.4)), Image.Resampling.LANCZOS)
        duration = gifEnemyNormal.info.get("duration", 5)  # duración por frame en ms
        pygame_frame = pygame.image.fromstring(resized_frame.tobytes(), resized_frame.size, resized_frame.mode)
        framesEnemyNormal.append(pygame_frame)
        durationsEnemyNormal.append(duration)
        gifEnemyNormal.seek(gifEnemyNormal.tell() + 1)
except EOFError:
    pass

frame_indexEnemyNormal = 0

gifEnemyBonnie = Image.open(get_resource_path("assets/bonnie_battle_sprite.gif"))
framesEnemyBonnie = []
durationsEnemyBonnie = []

try:
    while True:
        frame = gifEnemyBonnie.convert("RGBA")
        resized_frame = frame.resize((int(width * 0.45), int(height * 0.55)), Image.Resampling.LANCZOS)
        duration = gifEnemyBonnie.info.get("duration", 5)  # duración por frame en ms
        pygame_frame = pygame.image.fromstring(resized_frame.tobytes(), resized_frame.size, resized_frame.mode)
        framesEnemyBonnie.append(pygame_frame)
        durationsEnemyBonnie.append(duration)
        gifEnemyBonnie.seek(gifEnemyBonnie.tell() + 1)
except EOFError:
    pass

frame_indexEnemyBonnie = 0

gifEnemyChica = Image.open(get_resource_path("assets/chica_battle_sprite.gif"))
framesEnemyChica = []
durationsEnemyChica = []

try:
    while True:
        frame = gifEnemyChica.convert("RGBA")
        resized_frame = frame.resize((int(width * 0.55), int(height * 0.5)), Image.Resampling.LANCZOS)
        duration = gifEnemyChica.info.get("duration", 5)  # duración por frame en ms
        pygame_frame = pygame.image.fromstring(resized_frame.tobytes(), resized_frame.size, resized_frame.mode)
        framesEnemyChica.append(pygame_frame)
        durationsEnemyChica.append(duration)
        gifEnemyChica.seek(gifEnemyChica.tell() + 1)
except EOFError:
    pass

frame_indexEnemyChica = 0

gifEnemyFoxy = Image.open(get_resource_path("assets/foxy_battle_sprite.gif"))
framesEnemyFoxy = []
durationsEnemyFoxy = []

try:
    while True:
        frame = gifEnemyFoxy.convert("RGBA")
        resized_frame = frame.resize((int(width * 0.5), int(height * 0.4)), Image.Resampling.LANCZOS)
        duration = gifEnemyFoxy.info.get("duration", 5)  # duración por frame en ms
        pygame_frame = pygame.image.fromstring(resized_frame.tobytes(), resized_frame.size, resized_frame.mode)
        framesEnemyFoxy.append(pygame_frame)
        durationsEnemyFoxy.append(duration)
        gifEnemyFoxy.seek(gifEnemyFoxy.tell() + 1)
except EOFError:
    pass

frame_indexEnemyFoxy = 0


gifFredyCounter = Image.open(get_resource_path("assets/laughting_freedbear_final.gif"))
framesFredyCounter = []
durationsFredyCounter = []

try:
    while True:
        frame = gifFredyCounter.convert("RGBA")
        resized_frame = frame.resize((int(width * 0.5), int(height * 0.35)), Image.Resampling.LANCZOS)
        duration = gifFredyCounter.info.get("duration", 5)  # duración por frame en ms
        pygame_frame = pygame.image.fromstring(resized_frame.tobytes(), resized_frame.size, resized_frame.mode)
        framesFredyCounter.append(pygame_frame)
        durationsFredyCounter.append(duration)
        gifFredyCounter.seek(gifFredyCounter.tell() + 1)
except EOFError:
    pass

frame_indexFredyCounter = 0
#Square Black States
squareBlackFreddy = pygame.Surface((width * 0.1, height * 0.15)).convert_alpha()
squareBlackFreddy.fill((0,0,0))
squareBlackFreddy.blit(imageFreddyCharacter,(0,0))
squareBlackFreddy_rect = 0
squareBlack = pygame.Surface((width * 0.1, height * 0.15)).convert_alpha()
squareBlack.fill((0,0,0))

box_width = int(width * 0.65)
box_height = int(height * 0.32)
margin_size = width * 0.0025
# Crear el rectángulo del cuadro (área total incluyendo margen)
box_rect = pygame.Rect(
    (width - box_width) // 2.65 - margin_size,
    (height - box_height) // 22 - margin_size,
    box_width + margin_size * 2,
    box_height + margin_size * 2
)

# Crear el rectángulo interior (el cuadro negro)
inner_rect = pygame.Rect(
    box_rect.x + margin_size,
    box_rect.y + margin_size,
    box_width,
    box_height
)
#Music And Sounds
# Music And Sounds
background_music_game_init = pygame.mixer.Sound(get_resource_path("audio/musics/game_init_music.mp3"))
background_freedbear = pygame.mixer.Sound(get_resource_path("audio/musics/game_freedbear_music.mp3"))
counterMusicFreedbear = 0

background_music_map = pygame.mixer.Sound(get_resource_path("audio/musics/background_music_map.mp3"))
counterMusicMap = 0

background_mini_game_ballon_girl_music = pygame.mixer.Sound(get_resource_path("audio/musics/mini_game_ballon_girl_music.mp3"))
counter_background_mini_game_ballon_girl_music = 0

sfx_enter = pygame.mixer.Sound(get_resource_path("audio/sounds/enter_press_init.ogg"))
enter_attack_selections_sound = pygame.mixer.Sound(get_resource_path("audio/sounds/enter_attacks_selections_sound.mp3"))
enemy_attack_normal_audio = pygame.mixer.Sound(get_resource_path("audio/sounds/enemy_normal_attack_audio.mp3"))
enemy_attack_normal_audio_counter = 0

freddy_attack_sprite_1 = pygame.mixer.Sound(get_resource_path("audio/sounds/sound_attack_freddy_1_sprite.mp3"))
freddy_attack_sprite_2 = pygame.mixer.Sound(get_resource_path("audio/sounds/sound_attack_freddy_2_sprite.mp3"))
freddy_attack_sprite_3 = pygame.mixer.Sound(get_resource_path("audio/sounds/sound_attack_freddy_3_sprite.mp3"))
counter_sound_sprite1 = 0
counter_sound_sprite2 = 0
counter_sound_sprite3 = 0

enemy_damage_sound = pygame.mixer.Sound(get_resource_path("audio/sounds/enemy_damage_sound.mp3"))
counter_enemy_damage_sound = 0
enemy_dead_sound = pygame.mixer.Sound(get_resource_path("audio/sounds/dead_enemy_battle_sound.mp3"))
counter_enemy_dead_sound = 0

game_over = pygame.mixer.Sound(get_resource_path("audio/sounds/dead_sound_game_over.mp3"))
counter_game_over = 0

shop_freddy_mask = pygame.mixer.Sound(get_resource_path("audio/sounds/freddy_mask_shop_sound.mp3"))
counter_shop_freddy_mask = 0

chica_attack_sound = pygame.mixer.Sound(get_resource_path("audio/sounds/chica_battle_attack_sound.mp3"))
counter_chica_attack_sound = 0

bonnie_attack_sound = pygame.mixer.Sound(get_resource_path("audio/sounds/bonnie_battle_attack_sound.mp3"))
counter_bonnie_attack_sound = 0

bonnie_battle_music = pygame.mixer.Sound(get_resource_path("audio/musics/battle_music_bonnie.mp3"))
counter_bonnie_battle_music = 0

foxy_battle_music = pygame.mixer.Sound(get_resource_path("audio/musics/battle_music_foxy.mp3"))
counter_foxy_battle_music = 0

freedbear_sprite_map_music = pygame.mixer.Sound(get_resource_path("audio/musics/background_music_golden_freddy_sprite_map.mp3"))
counter_freedbear_sprite_map_music = 0

sound_ghost = pygame.mixer.Sound(get_resource_path("audio/sounds/ghost_sound.mp3"))
counter_sound_ghost = 0

final_battle_music = pygame.mixer.Sound(get_resource_path("audio/musics/background_music_final_battle.mp3"))
counter_final_battle_music = 0

winning_game_music = pygame.mixer.Sound(get_resource_path("audio/musics/background_music_complete_game.mp3"))
counter_winning_game_music = 0

winning_counter_music = pygame.mixer.Sound(get_resource_path("audio/musics/background_music_counter_complete_game.mp3"))
counter_winning__counter_music = 0

channel_music = pygame.mixer.Channel(0)
channel_sound = pygame.mixer.Channel(1)
channel_sound_battle = pygame.mixer.Channel(2)


running = True
hp_freddy = 100
hp_normal_enemy = 50
hp_chica = 500
hp_bonnie = 500
hp_foxy = 200
hp_final_enemy = 5
waitingGameOver = -1
counter_foxy_attack = 0
#Objects Map
masc_freddy_shop = False
unlock_padlock = False
defeat_bonnie = False
defeat_chica = False
defeat_foxy = False
defeat_final_enemy = False
waitingFinalEnemy = -1
winning_game = False
counterLastTime = 60
waitingCounterSeconds = -1
show_message_developer = False
while running:
    timeNow = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    #Events Keyboard 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # ENTER
                    if(gameVariables.isInitCompleteAnimations and waitingPassDialog == -1): # ENTER IN GAME INIT   
                        channel_sound.play(sfx_enter)
                        pygame.time.delay(300)
                        fade_surface = pygame.Surface((width, height))
                        fade_surface.fill((0, 0, 0))
                        for alpha in range(0, 256, 10):  
                            fade_surface.set_alpha(alpha)
                            screen.fill((255, 255, 255))  
                            screen.blit(backgroundInitGame, (width * 0.01, height * 0.01))
                            screen.blit(imageAllAnimatronicsInit, imageAllAnimatronicsInit_rect)
                            screen.blit(imageTittleStartInit, imageTittleStartInit_rect)
                            screen.blit(imageStartTittleInit, imageStartTittleInit_rect)
                            screen.blit(fade_surface, (0, 0)) 
                            pygame.display.flip()
                            pygame.time.delay(45)
                        screen.fill((0,0,0))
                        pygame.display.flip()
                        pygame.time.delay(300)
                        screen.fill((255,255,255))
                        screen.blit(backgroundInitGame, (width * 0.01, height * 0.01))
                        screen.blit(imageTittleGameSelection,imageTittleGameSelection_rect)
                        screen.blit(squareBlackFreddy,(width//16.5,height//5))
                        squareBlackFreddy_rect = squareBlackFreddy.get_rect(topleft=(width//16.5,height//5))
                        pygame.display.flip()
                        gameVariables.isInitGameSelection = False
                    if not gameVariables.isInitDialogFreedbear and gameVariables.isInitLoadWindow and timeNow >= waitingPassDialog and waitingPassDialog != -1 and waitingPassBackgroundFreddyAfterFreedbear == -1:
                        counterDialogFreedbear += 1
                        if(counterDialogFreedbear >= 5):
                            channel_sound.play(sfx_enter)
                            pygame.time.delay(300)
                            fade_surface = pygame.Surface((width, height))
                            fade_surface.fill((0, 0, 0))
                            for alpha in range(0, 256, 10):  
                                fade_surface.set_alpha(alpha)
                                screen.fill((255, 255, 255))  
                                screen.blit(backgroundFreedbear,(0,0))
                                pygame.draw.rect(screen, (255, 255, 255), box_rect)
                                pygame.draw.rect(screen, (0, 0, 0), inner_rect)
                                screen.blit(dialog_freedbear5, (inner_rect.x + (width * 0.015), inner_rect.y + (height * 0.02)))
                                screen.blit(buttonStartDialogFreedbear,(inner_rect.x + (width * 0.3), inner_rect.y + (height * 0.15)))
                                screen.blit(imageFreddyStatic,imageFreddyStatic_rect)
                                screen.blit(framesFreedbear[frame_indexFreedbear-1], (width//20, height//4)) 
                                screen.blit(fade_surface, (0, 0)) 
                                pygame.display.flip()
                                pygame.time.delay(5)
                            screen.fill((0,0,0))
                            pygame.display.flip()
                            pygame.time.delay(300)
                            gameVariables.isInitDialogFreedbear = True
                            gameVariables.isInitBackgroundAfterFreedbear = False
                            waitingPassBackgroundFreddyAfterFreedbear = timeNow + random.randint(25000, 40000)
                            channel_music.stop()
                        else:
                            waitingPassDialog = timeNow + 2000
                    if (gameVariables.isInitMiniGameBallonGirl and gameVariables.isInitCombat and gameVariables.isInitGameMap):
                        type_movement_heart = 0  
                        freedbear_center_x = imageFreedbearMiniGameBallonGirl_rect.x + movement_freedbear_mini_game_x + imageFreedbearMiniGameBallonGirl.get_width() // 2
                        heart_x = movement_heart_mini_game_x
                        heart_width = imageHeartMiniGameBallonGirl.get_width()
                        margin = heart_width * 0.25
                        left_limit = heart_x - margin
                        right_limit = heart_x + heart_width + margin
                        if left_limit <= freedbear_center_x <= right_limit:
                            unlock_padlock = True
                            waitingWordsCompleteMiniGame = timeNow + 2000
                        else:
                            hp_freddy = 0
                            gameVariables.isInitMiniGameBallonGirl = False
                            type_movement_heart = 1
                            movement_heart_mini_game_x = 0
                            movement_freedbear_mini_game_x = 0
                            gameVariables.isInitShopMangle = False
                            gameVariables.isInitShopBallonGirl = False
                            gameVariables.isInitCombat = True 
                            gameVariables.isInitGameMap = True
                            counter_background_mini_game_ballon_girl_music = 0
                            counterMusicMap = 0
                            counter_game_over = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left Click
                mouse_pos = pygame.mouse.get_pos()
                if squareBlackFreddy_rect.collidepoint(mouse_pos): # Click Freddy Icon
                    fade_surface = pygame.Surface((width, height))
                    fade_surface.fill((0, 0, 0))
                    for alpha in range(0, 256, 10):  
                        fade_surface.set_alpha(alpha)
                        screen.fill((255, 255, 255))  
                        screen.blit(backgroundInitGame, (width * 0.01, height * 0.01))
                        screen.blit(imageTittleGameSelection,imageTittleGameSelection_rect)
                        screen.blit(squareBlackFreddy,(width//16.5,height//5))
                        screen.blit(squareBlack,(width // 6.18,height//5))
                        screen.blit(squareBlack,(width // 3.8,height//5))
                        screen.blit(squareBlack,(width // 2.745,height//5))
                        screen.blit(squareBlack,(width // 2.145,height//5))
                        screen.blit(squareBlack,(width // 1.76,height//5))
                        screen.blit(fade_surface, (0, 0)) 
                        pygame.display.flip()
                        pygame.time.delay(10)
                    screen.fill((0,0,0))
                    channel_music.stop()
                    pygame.display.flip()
                    pygame.time.delay(300)
                    gameVariables.isInitLoadWindow = False
                if  not gameVariables.isInitCombat and gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear and waitingEnemyPosition != -1:
                    if imageAttackFreddySelection1_rect.collidepoint(mouse_pos):
                        attack_select_freddy = 1
                    elif imageAttackFreddySelection2_rect.collidepoint(mouse_pos):
                        attack_select_freddy = 2
                    elif imageAttackFreddySelection3_rect.collidepoint(mouse_pos):
                        attack_select_freddy = 3
                    end_animation_attacks = True 
                    waitingAnimationAttacksEnd = timeNow + 200
                    start_animation_attacks = False
                    waitingAnimationAttacksStart = -1
                if (gameVariables.isInitShopMangle or gameVariables.isInitShopBallonGirl) and gameVariables.isInitCombat and gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear:
                    if(imageButtonBackShop_rect.collidepoint(mouse_pos)):
                        gameVariables.isInitShopMangle = False
                        gameVariables.isInitShopBallonGirl = False
                        gameVariables.isInitCombat = True 
                        gameVariables.isInitGameMap = False
                        counterMusicMap = 0
                    if(imageFreddyMask_rect.collidepoint(mouse_pos) and not masc_freddy_shop and gameVariables.isInitShopMangle):
                        if(counter_shop_freddy_mask == 0):
                            channel_sound.play(shop_freddy_mask)
                            counter_shop_freddy_mask += 1
                        masc_freddy_shop = True
                    if(imageButtonPlay_rect.collidepoint(mouse_pos) and gameVariables.isInitShopBallonGirl and not gameVariables.isInitMiniGameBallonGirl and not unlock_padlock):
                        channel_sound.play(sfx_enter)
                        channel_music.stop()
                        gameVariables.isInitMiniGameBallonGirl = True 
                        gameVariables.isInitCombat = True 
                        gameVariables.isInitGameMap = True 
                        waitingBackgroundBallonGirl = -1
                        counter_background_mini_game_ballon_girl_music = 0



    #Events Keys Pressed 
    if keys[pygame.K_LEFT]:
        if(not gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear and not defeat_foxy):
            freddy_rect = imageFreddyCharacterLeft.get_rect(topleft=(
                imageFreddyCharacterLeft_rect.x + (movement_freddy_x - (width * 0.01)),
                imageFreddyCharacterLeft_rect.y + movement_freddy_y
            ))
            state_freddy_sprite = 1
            if(not freddy_rect.colliderect(imageBlockInMap_rect) or unlock_padlock):
                movement_freddy_x -= width * 0.01
                if random.random() < 0.025:
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    channel_music.stop()
                    state_battle_type = 0
                    counterMusicMap = 0
                if(freddy_rect.colliderect(imageBallonGirlInMap_rect) and (not defeat_bonnie or not defeat_chica)):
                    gameVariables.isInitShopBallonGirl = True
                    gameVariables.isInitCombat = True 
                    gameVariables.isInitGameMap = True
                    waitingBackgroundBallonGirl = timeNow + 2000 
                if(freddy_rect.colliderect(imageMangleInMap_rect) and (not defeat_bonnie or not defeat_chica)):
                    gameVariables.isInitShopMangle = True
                    gameVariables.isInitCombat = True 
                    gameVariables.isInitGameMap = True
                if(freddy_rect.colliderect(imageBonnieInMap_rect) and not defeat_bonnie):
                    if(unlock_padlock and masc_freddy_shop):
                        gameVariables.isInitCombat = False
                        gameVariables.isInitGameMap = True
                        waitingEnemyPosition = timeNow + 200
                        state_battle_type = 1
                        channel_music.stop()
                        counterMusicMap = 0
                    else:
                        hp_freddy = 0
                        gameVariables.isInitMiniGameBallonGirl = False
                        type_movement_heart = 1
                        movement_heart_mini_game_x = 0
                        movement_freedbear_mini_game_x = 0
                        gameVariables.isInitShopMangle = False
                        gameVariables.isInitShopBallonGirl = False
                        gameVariables.isInitCombat = True 
                        gameVariables.isInitGameMap = True
                        counter_background_mini_game_ballon_girl_music = 0
                        counterMusicMap = 0
                        counter_game_over = 0
                if(freddy_rect.colliderect(imageShadowInMap_rect) and not defeat_chica):
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    state_battle_type = 2
                    channel_music.stop()
                    counterMusicMap = 0
                if(freddy_rect.colliderect(imageFoxyInMap_rect) and defeat_bonnie and defeat_chica):
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    state_battle_type = 3
                    channel_music.stop()
                    counterMusicMap = 0
        if(gameVariables.isInitMiniGameBallonGirl and gameVariables.isInitCombat and gameVariables.isInitGameMap):
            freedbear_rect_mini_game = imageFreedbearMiniGameBallonGirl.get_rect(topleft=(
                imageFreedbearMiniGameBallonGirl_rect.x + (movement_freedbear_mini_game_x - (width * 0.002)),
                imageFreedbearMiniGameBallonGirl_rect.y + movement_freddy_y
            ))
            if(freedbear_rect_mini_game.x > 0):
                movement_freedbear_mini_game_x -= width * 0.002
        if(defeat_foxy and defeat_chica and defeat_bonnie and not gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear):
            movement_golden_freddy_map_x -= width * 0.01
            if(waitingGhost == -1):
                waitingGhost = timeNow + 5000

               
    if keys[pygame.K_RIGHT]:
        if(not gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear and not defeat_foxy):
            freddy_rect = imageFreddyCharacterLeft.get_rect(topleft=(
                imageFreddyCharacterLeft_rect.x + (movement_freddy_x + (width * 0.01)),
                imageFreddyCharacterLeft_rect.y + movement_freddy_y
            ))
            state_freddy_sprite = 2
            if(not freddy_rect.colliderect(imageBlockInMap_rect) or unlock_padlock):
                movement_freddy_x += width * 0.01
                if random.random() < 0.025:
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    state_battle_type = 0
                    channel_music.stop()
                    counterMusicMap = 0
                if(freddy_rect.colliderect(imageBallonGirlInMap_rect) and (not defeat_bonnie or not defeat_chica)):
                    gameVariables.isInitShopBallonGirl = True
                    gameVariables.isInitCombat = True 
                    gameVariables.isInitGameMap = True 
                    waitingBackgroundBallonGirl = timeNow + 2000 
                if(freddy_rect.colliderect(imageMangleInMap_rect) and (not defeat_bonnie or not defeat_chica)):
                    gameVariables.isInitShopMangle = True
                    gameVariables.isInitCombat = True 
                    gameVariables.isInitGameMap = True
                if(freddy_rect.colliderect(imageBonnieInMap_rect) and not defeat_bonnie):
                    if(unlock_padlock and masc_freddy_shop):
                        gameVariables.isInitCombat = False
                        gameVariables.isInitGameMap = True
                        waitingEnemyPosition = timeNow + 200
                        state_battle_type = 1
                        channel_music.stop()
                        counterMusicMap = 0
                    else:
                        hp_freddy = 0
                        gameVariables.isInitMiniGameBallonGirl = False
                        type_movement_heart = 1
                        movement_heart_mini_game_x = 0
                        movement_freedbear_mini_game_x = 0
                        gameVariables.isInitShopMangle = False
                        gameVariables.isInitShopBallonGirl = False
                        gameVariables.isInitCombat = True 
                        gameVariables.isInitGameMap = True
                        counter_background_mini_game_ballon_girl_music = 0
                        counterMusicMap = 0
                        counter_game_over = 0
                if(freddy_rect.colliderect(imageShadowInMap_rect) and not defeat_chica):
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    state_battle_type = 2
                    channel_music.stop()
                    counterMusicMap = 0
                if(freddy_rect.colliderect(imageFoxyInMap_rect) and defeat_bonnie and defeat_chica):
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    state_battle_type = 3
                    channel_music.stop()
                    counterMusicMap = 0
        if(gameVariables.isInitMiniGameBallonGirl and gameVariables.isInitCombat and gameVariables.isInitGameMap):
            freedbear_rect_mini_game = imageFreedbearMiniGameBallonGirl.get_rect(topleft=(
                imageFreedbearMiniGameBallonGirl_rect.x + (movement_freedbear_mini_game_x + (width * 0.002)),
                imageFreedbearMiniGameBallonGirl_rect.y + movement_freddy_y
            ))
            if(freedbear_rect_mini_game.x < (width - width * 0.52)):
                movement_freedbear_mini_game_x += width * 0.002
        if(defeat_foxy and defeat_chica and defeat_bonnie and not gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear):
            movement_golden_freddy_map_x += width * 0.01
            if(waitingGhost == -1):
                waitingGhost = timeNow + 5000
    if keys[pygame.K_UP]:
        if(not gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear and not defeat_foxy):
            freddy_rect = imageFreddyCharacterLeft.get_rect(topleft=(
                imageFreddyCharacterLeft_rect.x + movement_freddy_x,
                imageFreddyCharacterLeft_rect.y + (movement_freddy_y - (height * 0.01))
            ))
            state_freddy_sprite = 3
            if(not freddy_rect.colliderect(imageBlockInMap_rect) or unlock_padlock):
                movement_freddy_y -= height * 0.01
                if random.random() < 0.025:
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    channel_music.stop()
                    state_battle_type = 0
                    counterMusicMap = 0
                if(freddy_rect.colliderect(imageBallonGirlInMap_rect) and (not defeat_bonnie or not defeat_chica)):
                    gameVariables.isInitShopBallonGirl = True
                    gameVariables.isInitCombat = True 
                    waitingBackgroundBallonGirl = timeNow + 2000 
                    gameVariables.isInitGameMap = True 
                if(freddy_rect.colliderect(imageMangleInMap_rect) and (not defeat_bonnie or not defeat_chica)):
                    gameVariables.isInitShopMangle = True
                    gameVariables.isInitCombat = True 
                    gameVariables.isInitGameMap = True
                if(freddy_rect.colliderect(imageBonnieInMap_rect) and not defeat_bonnie):
                    if(unlock_padlock and masc_freddy_shop):
                        gameVariables.isInitCombat = False
                        gameVariables.isInitGameMap = True
                        waitingEnemyPosition = timeNow + 200
                        state_battle_type = 1
                        channel_music.stop()
                        counterMusicMap = 0
                    else:
                        hp_freddy = 0
                        gameVariables.isInitMiniGameBallonGirl = False
                        type_movement_heart = 1
                        movement_heart_mini_game_x = 0
                        movement_freedbear_mini_game_x = 0
                        gameVariables.isInitShopMangle = False
                        gameVariables.isInitShopBallonGirl = False
                        gameVariables.isInitCombat = True 
                        gameVariables.isInitGameMap = True
                        counter_background_mini_game_ballon_girl_music = 0
                        counterMusicMap = 0
                        counter_game_over = 0
                if(freddy_rect.colliderect(imageShadowInMap_rect) and not defeat_chica):
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    state_battle_type = 2
                    channel_music.stop()
                    counterMusicMap = 0
                if(freddy_rect.colliderect(imageFoxyInMap_rect) and defeat_bonnie and defeat_chica):
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    state_battle_type = 3
                    channel_music.stop()
                    counterMusicMap = 0
        if(defeat_foxy and defeat_chica and defeat_bonnie and not gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear):
            movement_golden_freddy_map_y -= height * 0.01
            if(waitingGhost == -1):
                waitingGhost = timeNow + 5000
    if keys[pygame.K_DOWN]:
        if(not gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear and not defeat_foxy):
            freddy_rect = imageFreddyCharacterLeft.get_rect(topleft=(
                imageFreddyCharacterLeft_rect.x + movement_freddy_x,
                imageFreddyCharacterLeft_rect.y + (movement_freddy_y + (height * 0.01))
            ))
            state_freddy_sprite = 4
            if(not freddy_rect.colliderect(imageBlockInMap_rect) or unlock_padlock):
                movement_freddy_y += height * 0.01
                if random.random() < 0.025:
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    state_battle_type = 0
                    channel_music.stop()
                    counterMusicMap = 0
                if(freddy_rect.colliderect(imageBallonGirlInMap_rect) and (not defeat_bonnie or not defeat_chica)):
                    gameVariables.isInitShopBallonGirl = True
                    gameVariables.isInitCombat = True
                    waitingBackgroundBallonGirl = timeNow + 2000 
                    gameVariables.isInitGameMap = True 
                if(freddy_rect.colliderect(imageMangleInMap_rect) and (not defeat_bonnie or not defeat_chica)):
                    gameVariables.isInitShopMangle = True
                    gameVariables.isInitCombat = True 
                    gameVariables.isInitGameMap = True
                if(freddy_rect.colliderect(imageBonnieInMap_rect) and not defeat_bonnie):
                    if(unlock_padlock and masc_freddy_shop):
                        gameVariables.isInitCombat = False
                        gameVariables.isInitGameMap = True
                        waitingEnemyPosition = timeNow + 200
                        state_battle_type = 1
                        channel_music.stop()
                        counterMusicMap = 0
                    else:
                        hp_freddy = 0
                        gameVariables.isInitMiniGameBallonGirl = False
                        type_movement_heart = 1
                        movement_heart_mini_game_x = 0
                        movement_freedbear_mini_game_x = 0
                        gameVariables.isInitShopMangle = False
                        gameVariables.isInitShopBallonGirl = False
                        gameVariables.isInitCombat = True 
                        gameVariables.isInitGameMap = True
                        counter_background_mini_game_ballon_girl_music = 0
                        counterMusicMap = 0
                        counter_game_over = 0
                if(freddy_rect.colliderect(imageShadowInMap_rect) and not defeat_chica):
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    state_battle_type = 2
                    channel_music.stop()
                    counterMusicMap = 0
                if(freddy_rect.colliderect(imageFoxyInMap_rect) and defeat_bonnie and defeat_chica):
                    gameVariables.isInitCombat = False
                    gameVariables.isInitGameMap = True
                    waitingEnemyPosition = timeNow + 200
                    state_battle_type = 3
                    channel_music.stop()
                    counterMusicMap = 0
        if(defeat_foxy and defeat_chica and defeat_bonnie and not gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear):
            movement_golden_freddy_map_y += height * 0.01
            if(waitingGhost == -1):
                waitingGhost = timeNow + 5000

    if not gameVariables.isInitMusicWarning and timeNow - start_time >= waitingTimeInitSound:
        pygame.mixer.music.load(get_resource_path("audio/sounds/init_audio_game.mp3"))     
        pygame.mixer.music.set_volume(1)         
        pygame.mixer.music.play()
        gameVariables.isInitMusicWarning = True
    
    if not gameVariables.isInitWarning and timeNow - start_time >= waitingTimeInitWarning:
        screen.blit(warningInit,warningInit_rect)
        pygame.display.flip()
        gameVariables.isInitWarning = True

    if not gameVariables.isInitFadeInOutWarning and timeNow - start_time >= waitingTimeInitFadeInOut:      
        for alpha in range(255, -1, -5):
            warningInit.set_alpha(alpha)
            screen.fill((0, 0, 0))
            screen.blit(warningInit, warningInit_rect)
            pygame.display.flip()
            pygame.time.delay(30)
            gameVariables.isInitFadeInOutWarning = True

    if not gameVariables.isInitGameTittle and timeNow - start_time >= waitingTimeInitGame:   
        channel_music.play(background_music_game_init,loops=-1)
        screen.fill((255,255,255))
        screen.blit(backgroundInitGame,(width * 0.01,height * 0.01))
        pygame.display.flip()
        anim_x_tittle = -imageTittleStartInit_rect.width   
        anim_y_robots = height + imageAllAnimatronicsInit_rect.height  

        final_x_tittle = imageTittleStartInit_rect.x
        final_y_robots = imageAllAnimatronicsInit_rect.y

        speed = 20

        while anim_x_tittle < final_x_tittle or anim_y_robots > final_y_robots:
            screen.fill((255,255,255))
            screen.blit(backgroundInitGame,(width * 0.01,height * 0.01))

            if anim_x_tittle < final_x_tittle:
                anim_x_tittle += speed
                if anim_x_tittle > final_x_tittle:
                    anim_x_tittle = final_x_tittle
            screen.blit(imageTittleStartInit, (anim_x_tittle, imageTittleStartInit_rect.y))

            if anim_y_robots > final_y_robots:
                anim_y_robots -= speed
                if anim_y_robots < final_y_robots:
                    anim_y_robots = final_y_robots
            screen.blit(imageAllAnimatronicsInit, (imageAllAnimatronicsInit_rect.x, anim_y_robots))

            pygame.display.flip()
            pygame.time.delay(30)
        gameVariables.isInitGameTittle = True

    if not gameVariables.isInitCompleteAnimations and timeNow - start_time >= waitingCompleteAnimationsInit:
        for repeat in range(0,6):
            screen.fill((255,255,255))
            screen.blit(backgroundInitGame,(width * 0.01,height * 0.01))
            screen.blit(imageAllAnimatronicsInit, imageAllAnimatronicsInit_rect)
            screen.blit(imageTittleStartInit, imageTittleStartInit_rect)
            if(repeat % 2 == 0):
                imageStartTittleInit.set_alpha(0)
                screen.blit(imageStartTittleInit,imageStartTittleInit_rect)   
            else:
                imageStartTittleInit.set_alpha(255)
                screen.blit(imageStartTittleInit,imageStartTittleInit_rect)
            pygame.display.flip()   
            pygame.time.delay(250)        
        imageStartTittleInit.set_alpha(255)
        screen.blit(imageStartTittleInit,imageStartTittleInit_rect)
        pygame.display.flip() 
        gameVariables.isInitCompleteAnimations = True
    if not gameVariables.isInitGameSelection:
        separationSquaresWidth = 0
        for squaresCount in range(0,5):
            if(squaresCount == 0):
                screen.blit(squareBlack,(width // 6.18,height//5))
            elif(squaresCount == 1):
                screen.blit(squareBlack,(width // 3.8,height//5))
            elif(squaresCount == 2):
                screen.blit(squareBlack,(width // 2.745,height//5))
            elif(squaresCount == 3):
                screen.blit(squareBlack,(width // 2.145,height//5))
            elif(squaresCount == 4):
                screen.blit(squareBlack,(width // 1.76,height//5))
            pygame.display.flip()   
            pygame.time.delay(100)
        gameVariables.isInitGameSelection = True
    if not gameVariables.isInitLoadWindow:
        waitingScreenLoading = timeNow + random.randint(25000, 40000)
        screen.fill((0,0,0))
        screen.blit(backgroundLoadingScreen,(0,0))
        screen.blit(imageTittleLoadingScreen1, imageTittleLoadingScreen1_rect)
        screen.blit(imageFooterLoadingScreen1, imageFooterLoadingScreen1_rect)
        screen.blit(imageAnimatronicLoadingScreen1, imageAnimatronicLoadingScreen1_rect)
        pygame.display.flip()
        gameVariables.isInitLoadWindow = True
    if not gameVariables.isInitDialogFreedbear and gameVariables.isInitLoadWindow and timeNow >= waitingScreenLoading and waitingScreenLoading != -1:
        if(counterMusicFreedbear == 0):
            counterMusicFreedbear +=1
            waitingPassDialog = timeNow + 2000
            channel_music.play(background_freedbear,loops=-1)
        screen.fill((0,0,0))
        screen.blit(backgroundFreedbear,(0,0))
        pygame.draw.rect(screen, (255, 255, 255), box_rect)
        pygame.draw.rect(screen, (0, 0, 0), inner_rect)
        if(counterDialogFreedbear == 0):
            screen.blit(dialog_freedbear1, (inner_rect.x + (width * 0.015), inner_rect.y + (height * 0.02)))
        elif(counterDialogFreedbear == 1):
            screen.blit(dialog_freedbear2, (inner_rect.x + (width * 0.015), inner_rect.y + (height * 0.02)))
        elif(counterDialogFreedbear == 2):
            screen.blit(dialog_freedbear3, (inner_rect.x + (width * 0.015), inner_rect.y + (height * 0.02)))
        elif(counterDialogFreedbear == 3):
            screen.blit(dialog_freedbear4, (inner_rect.x + (width * 0.015), inner_rect.y + (height * 0.02)))
        elif(counterDialogFreedbear == 4):
            screen.blit(dialog_freedbear5, (inner_rect.x + (width * 0.015), inner_rect.y + (height * 0.02)))
            screen.blit(buttonStartDialogFreedbear,(inner_rect.x + (width * 0.3), inner_rect.y + (height * 0.15)))
        if(timeNow >= waitingPassDialog and waitingPassDialog != -1 and counterDialogFreedbear < 4):
            screen.blit(imageArrowPassDialogFreedbear, (inner_rect.x + (width * 0.28), inner_rect.y + (height * 0.217)))
        screen.blit(imageFreddyStatic,imageFreddyStatic_rect)
        if(frame_indexFreedbear >= len(framesFreedbear)):
            frame_indexFreedbear = 0
        else:
            frame_indexFreedbear +=1  
        screen.blit(framesFreedbear[frame_indexFreedbear-1], (width//20, height//4)) 
        pygame.time.delay(durationsFreedbear[frame_indexFreedbear-1])
        pygame.display.flip()
    if not gameVariables.isInitBackgroundAfterFreedbear and gameVariables.isInitLoadWindow:
        if(timeNow >= waitingPassBackgroundFreddyAfterFreedbear):
            fade_surface = pygame.Surface((width, height))
            fade_surface.fill((0, 0, 0))
            for alpha in range(0, 256, 10):  
                fade_surface.set_alpha(alpha)
                screen.fill((0, 0, 0))  
                screen.blit(backgroundFreddyAfterFreedbear,(0,0))
                screen.blit(fade_surface, (0, 0)) 
                pygame.display.flip()
                pygame.time.delay(5)
            screen.fill((0,0,0))
            pygame.display.flip()
            pygame.time.delay(300)
            gameVariables.isInitBackgroundAfterFreedbear = True
            gameVariables.isInitGameMap = False
        else:
            screen.fill((0,0,0))
            screen.blit(backgroundFreddyAfterFreedbear,(0,0))
            pygame.display.flip()
    if not gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear:
        if(not defeat_foxy):
            if(counterMusicMap == 0):
                counterMusicMap +=1
                channel_music.play(background_music_map,loops=-1)
            screen.fill((0,0,0))
            if(not defeat_bonnie or not defeat_chica):
                screen.blit(backgroundMap,(0,0))
                if(state_freddy_sprite == 1):
                    screen.blit(imageFreddyCharacterLeft,(imageFreddyCharacterLeft_rect.x + movement_freddy_x,imageFreddyCharacterLeft_rect.y + movement_freddy_y))
                elif(state_freddy_sprite == 2):
                    screen.blit(imageFreddyCharacterRight,(imageFreddyCharacterLeft_rect.x + movement_freddy_x,imageFreddyCharacterLeft_rect.y + movement_freddy_y))
                elif(state_freddy_sprite == 3):
                    screen.blit(imageFreddyCharacterTop,(imageFreddyCharacterLeft_rect.x + movement_freddy_x,imageFreddyCharacterLeft_rect.y + movement_freddy_y))
                elif(state_freddy_sprite == 4):
                    screen.blit(imageFreddyCharacterBottom,(imageFreddyCharacterLeft_rect.x + movement_freddy_x,imageFreddyCharacterLeft_rect.y + movement_freddy_y))
                screen.blit(imageMangleInMap,imageMangleInMap_rect)
                if(not defeat_bonnie):
                    screen.blit(imageBonnieInMap,imageBonnieInMap_rect)
                if(not unlock_padlock):
                    screen.blit(imageBlockInMap,imageBlockInMap_rect)
                if(not defeat_chica):
                    screen.blit(imageShadowInMap,imageShadowInMap_rect)
                screen.blit(imageBallonGirlInMap,imageBallonGirlInMap_rect)
            else:
                screen.blit(backgroundFoxyMap,(0,0))
                screen.blit(imageFoxyInMap,imageFoxyInMap_rect)
                if(state_freddy_sprite == 1):
                    screen.blit(imageFreddyCharacterLeft,(imageFreddyCharacterLeft_rect.x + movement_freddy_x,imageFreddyCharacterLeft_rect.y + movement_freddy_y))
                elif(state_freddy_sprite == 2):
                    screen.blit(imageFreddyCharacterRight,(imageFreddyCharacterLeft_rect.x + movement_freddy_x,imageFreddyCharacterLeft_rect.y + movement_freddy_y))
                elif(state_freddy_sprite == 3):
                    screen.blit(imageFreddyCharacterTop,(imageFreddyCharacterLeft_rect.x + movement_freddy_x,imageFreddyCharacterLeft_rect.y + movement_freddy_y))
                elif(state_freddy_sprite == 4):
                    screen.blit(imageFreddyCharacterBottom,(imageFreddyCharacterLeft_rect.x + movement_freddy_x,imageFreddyCharacterLeft_rect.y + movement_freddy_y))
        else:
            if(counter_freedbear_sprite_map_music == 0):
                channel_music.play(freedbear_sprite_map_music,loops=-1)
                counter_freedbear_sprite_map_music += 1
            screen.fill((0,0,0))
            screen.blit(imageSpriteGoldenFreddyInMap,(imageSpriteGoldenFreddyInMap_rect.x + movement_golden_freddy_map_x,imageSpriteGoldenFreddyInMap_rect.y + movement_golden_freddy_map_y))
            draw_crt_lines(screen, width, height)
            if(waitingGhost != -1):
                elapsed_time = timeNow - waitingGhost
                if elapsed_time > 0 and elapsed_time < 250:
                    if(counter_sound_ghost == 0):
                        channel_sound.play(sound_ghost)
                        counter_sound_ghost += 1
                    screen.blit(imageGhostPart1,(width//4,height // 6.5))
                elif elapsed_time >= 250 and elapsed_time < 500:
                    screen.blit(imageGhostPart2,(width//4,height // 6.5))
                elif elapsed_time >= 500:
                    waitingGhost = -1
                    gameVariables.isInitGameMap = True
                    waitingEnterFinalBattle = timeNow + 3500
        pygame.display.flip()
        pygame.time.delay(250)
    if not gameVariables.isInitCombat and gameVariables.isInitGameMap and gameVariables.isInitBackgroundAfterFreedbear and waitingEnemyPosition != -1:
        current_hp = (
                    hp_normal_enemy if state_battle_type == 0
                    else hp_bonnie if state_battle_type == 1
                    else hp_chica if state_battle_type == 2
                    else hp_foxy if state_battle_type == 3
                    else hp_final_enemy
        )
        if(state_battle_type == 1):
            if(counter_bonnie_battle_music == 0):
                channel_music.play(bonnie_battle_music,loops=-1)
                counter_bonnie_battle_music += 1
        if(state_battle_type == 3):
            if(counter_foxy_battle_music == 0):
                channel_music.play(foxy_battle_music,loops=-1)
                counter_foxy_battle_music += 1
        if(state_battle_type == 4):
            if(counter_final_battle_music == 0):
                channel_music.play(final_battle_music,loops=-1)
                counter_final_battle_music += 1
        screen.fill((0,0,0))
        if(counter_game_over == 1):
            counter_game_over = 0
        if(state_battle_type == 0 or state_battle_type == 1 or state_battle_type == 2):
            screen.blit(backgroundBattle,(0,0))
        if(masc_freddy_shop and state_battle_type != 3 and state_battle_type != 4):
            screen.blit(imageFreddyMask,(width// 1.55,height// 8))
        if((start_animation_attacks and waitingAnimationAttacksStart != -1) or (end_animation_attacks and waitingAnimationAttacksEnd != -1)):
            if(end_animation_attacks and waitingAnimationAttacksEnd != -1):
                elapsed_time = timeNow - waitingAnimationAttacksEnd
                if elapsed_time < 250:
                    progress = elapsed_time / 250
                    current_alpha = int(255 * ( 1 - progress))
                    imageAttackFreddySelection1.set_alpha(current_alpha)
                    imageAttackFreddySelection2.set_alpha(current_alpha)
                    imageAttackFreddySelection3.set_alpha(current_alpha)
                    if(attack_select_freddy == 1):
                        imageAttackFreddySelection1 = pygame.transform.scale(imageAttackFreddySelection1, (imageAttackFreddySelection1.get_width() + (width * 0.01), imageAttackFreddySelection1.get_height() + (height * 0.01)))
                    elif(attack_select_freddy == 2):
                        imageAttackFreddySelection2 = pygame.transform.scale(imageAttackFreddySelection2, (imageAttackFreddySelection2.get_width() + (width * 0.01), imageAttackFreddySelection2.get_height() + (height * 0.01)))
                    elif(attack_select_freddy == 3):
                        imageAttackFreddySelection3 = pygame.transform.scale(imageAttackFreddySelection3, (imageAttackFreddySelection3.get_width() + (width * 0.01), imageAttackFreddySelection3.get_height() + (height * 0.01)))
                    screen.blit(imageAttackFreddySelection1,imageAttackFreddySelection1_rect) 
                    screen.blit(imageAttackFreddySelection2,imageAttackFreddySelection2_rect) 
                    screen.blit(imageAttackFreddySelection3,imageAttackFreddySelection3_rect) 
                    if(elapsed_time <= 200):
                        animate_freddy_attack = True
                        animate_freddy_attack_waiting = timeNow
                elif elapsed_time >= 3000:
                    end_animation_attacks = False
                    waitingAnimationAttacksEnd = -1
                    if(attack_select_freddy == 1):
                        imageAttackFreddySelection1 = pygame.image.load(get_resource_path("assets/attack_selection_1_battle.png")).convert_alpha()
                        imageAttackFreddySelection1 = pygame.transform.scale(imageAttackFreddySelection1,(width * 0.35,height * 0.12))
                    elif(attack_select_freddy == 2):
                        imageAttackFreddySelection2 = pygame.image.load(get_resource_path("assets/attack_selection_2_battle.png")).convert_alpha()
                        imageAttackFreddySelection2 = pygame.transform.scale(imageAttackFreddySelection2,(width * 0.35,height * 0.12))
                    elif(attack_select_freddy == 3):
                        imageAttackFreddySelection3 = pygame.image.load(get_resource_path("assets/attack_selection_3_battle.png")).convert_alpha()
                        imageAttackFreddySelection3 = pygame.transform.scale(imageAttackFreddySelection3,(width * 0.35,height * 0.12))
            elif(start_animation_attacks and waitingAnimationAttacksStart != -1 and current_hp > 0):
                elapsed_time = timeNow - waitingAnimationAttacksStart
                if elapsed_time < 350:
                    progress = elapsed_time / 350
                    current_alpha = int(255 * progress)
                    imageAttackFreddySelection1.set_alpha(current_alpha)
                    imageAttackFreddySelection2.set_alpha(current_alpha)
                    imageAttackFreddySelection3.set_alpha(current_alpha)
                    screen.blit(imageAttackFreddySelection1,imageAttackFreddySelection1_rect) 
                    screen.blit(imageAttackFreddySelection2,imageAttackFreddySelection2_rect) 
                    screen.blit(imageAttackFreddySelection3,imageAttackFreddySelection3_rect) 
                else:
                    if(audio_counter_sound_attacks_selection == 0):
                        audio_counter_sound_attacks_selection +=1
                        channel_sound.play(enter_attack_selections_sound)
                    imageAttackFreddySelection1.set_alpha(255)
                    imageAttackFreddySelection2.set_alpha(255)
                    imageAttackFreddySelection3.set_alpha(255)
                    screen.blit(imageAttackFreddySelection1,imageAttackFreddySelection1_rect) 
                    screen.blit(imageAttackFreddySelection2,imageAttackFreddySelection2_rect) 
                    screen.blit(imageAttackFreddySelection3,imageAttackFreddySelection3_rect) 
        if(animate_freddy_attack):
            if(timeNow <= animate_freddy_attack_waiting + 100):
                screen.blit(imageFreddyAttackFrame1,imageFreddyAttackFrame1_rect) 
            elif(timeNow >= animate_freddy_attack_waiting + 101 and timeNow <= animate_freddy_attack_waiting + 200):
                screen.blit(imageFreddyAttackFrame2,imageFreddyAttackFrame2_rect) 
            elif(timeNow >= animate_freddy_attack_waiting + 201 and timeNow <= animate_freddy_attack_waiting + 300):
                screen.blit(imageFreddyAttackFrame3,imageFreddyAttackFrame3_rect) 
            elif(timeNow >= animate_freddy_attack_waiting + 301 and timeNow <= animate_freddy_attack_waiting + 1000):
                screen.blit(imageFreddyAttackFrame4,imageFreddyAttackFrame4_rect) 
            elif(timeNow >= animate_freddy_attack_waiting + 1001):
                animate_freddy_attack = False
                enter_to_attack_freddy = True
                waitingEnterToAttackFreddy = timeNow + 300
                if(attack_select_freddy == 1):
                    enemyIsInAttackWaiting = timeNow + 1000
                    enemy_is_in_attack = True
                elif(attack_select_freddy == 2):
                    enemyIsInAttackWaiting = timeNow + 2500
                    enemy_is_in_attack = True

        else:
            screen.blit(imageFreddyStatic,imageFreddyStatic_rect)
        if(timeNow < waitingEnemyPosition):
            time = timeNow / waitingEnemyPosition
            current_x = 0
            current_y = 0
            if(state_battle_type == 0):
                current_x = (width - (width * 35)) + ((width//15) - (width - (width * 35))) * time
                current_y = (height // 4) + ((height//2.4) - (height // 4)) * time
            elif(state_battle_type == 1):
                current_x = (width - (width * 35)) + ((-(width * 0.11)) - (width - (width * 35))) * time
                current_y = (height // 4) + ((height//2.4) - (height // 4)) * time
            elif(state_battle_type == 2):
                current_x = (width - (width * 35)) + ((-(width * 0.11)) - (width - (width * 35))) * time
                current_y = (height // 4) + ((height//2.4) - (height // 4)) * time
            elif(state_battle_type == 3):
                current_x = (width - (width * 35)) + ((-(width * 0.11)) - (width - (width * 35))) * time
                current_y = (height // 4) + ((height//2.4) - (height // 4)) * time
            if(state_battle_type == 0):
                screen.blit(framesEnemyNormal[0], (current_x, current_y))
            elif(state_battle_type == 1):
                screen.blit(framesEnemyBonnie[0], (current_x, current_y))
            elif(state_battle_type == 2):
                screen.blit(framesEnemyChica[0], (current_x, current_y))
            elif(state_battle_type == 3):
                screen.blit(framesEnemyFoxy[0], (current_x, current_y))
            elif(state_battle_type == 4):
                screen.blit(imageGoldenFreddyBattle, imageGoldenFreddyBattle_rect)
        else:
            if(not start_animation_attacks and waitingAnimationAttacksStart == -1):
                start_animation_attacks = True
                waitingAnimationAttacksStart = timeNow + 1000
            if(waitingEnemyAttack == -1):
                if(state_battle_type == 4):
                    waitingEnemyAttack = timeNow + random.randint(0,10)
                else:    
                    waitingEnemyAttack = timeNow + random.randint(3000,12000)
            if(state_battle_type == 0):
                if(frame_indexEnemyNormal >= len(framesEnemyNormal)):
                    frame_indexEnemyNormal = 0
                else:
                    frame_indexEnemyNormal +=1
            elif(state_battle_type == 1):
                if(frame_indexEnemyBonnie >= len(framesEnemyBonnie)):
                    frame_indexEnemyBonnie = 0
                else:
                    frame_indexEnemyBonnie +=1
            elif(state_battle_type == 2):
                if(frame_indexEnemyChica >= len(framesEnemyChica)):
                    frame_indexEnemyChica = 0
                else:
                    frame_indexEnemyChica +=1
            elif(state_battle_type == 3):
                if(frame_indexEnemyFoxy >= len(framesEnemyFoxy)):
                    frame_indexEnemyFoxy = 0
                else:
                    frame_indexEnemyFoxy +=1
            if(timeNow >= waitingEnemyAttack and waitingEnemyAttack != -1 and current_hp > 0):
                if(state_battle_type == 0):
                    elapsed = timeNow - waitingEnemyAttack
                    animation_duration = 500
                    movement_distance = width * 0.2
                    if elapsed < animation_duration:
                        progress = elapsed / animation_duration
                        if elapsed < animation_duration / 2:
                            move = int(movement_distance * (progress * 2)) 
                            if(elapsed <= (animation_duration/2) - 50):
                                if(enemy_attack_normal_audio_counter == 0):
                                    channel_sound.play(enemy_attack_normal_audio)
                                    enemy_attack_normal_audio_counter +=1
                                    attack_type = random.randint(1, 4)
                                    if(attack_type < 4):
                                        hp_freddy -= 5
                                    else:
                                        hp_freddy -= 10
                                if(attack_type < 4):
                                    screen.blit(imageAttackEnemyNormal1,imageAttackEnemyNormal1_rect)
                                else:
                                    screen.blit(imageAttackEnemyNormal2,imageAttackEnemyNormal2_rect)
                        else:
                            if(elapsed <= (animation_duration/2) + 50):
                                if(attack_type < 4):
                                    screen.blit(imageAttackEnemyNormal1,imageAttackEnemyNormal1_rect)
                                else:
                                    screen.blit(imageAttackEnemyNormal2,imageAttackEnemyNormal2_rect)
                                if(enemy_attack_normal_audio_counter == 1):
                                    enemy_attack_normal_audio_counter = 0
                            move = int(movement_distance * (2 - progress * 2)) 
                        enemy_x = (width // 15) + move
                        enemy_y = height // 2.4
                        screen.blit(framesEnemyNormal[frame_indexEnemyNormal-1], (enemy_x, enemy_y))
                        pygame.time.delay(durationsEnemyNormal[frame_indexEnemyNormal-1])
                    else:
                        waitingEnemyAttack = -1
                        counter_chica_attack_sound = 0
                        counter_bonnie_attack_sound = 0
                        counter_foxy_attack = 0
                        if(state_battle_type == 0):
                            screen.blit(framesEnemyNormal[frame_indexEnemyNormal-1], (width//15, height//2.4))
                        elif(state_battle_type == 1):
                            screen.blit(framesEnemyBonnie[frame_indexEnemyBonnie-1], (-(width * 0.08), height//3.5))
                        elif(state_battle_type == 2):
                            screen.blit(framesEnemyChica[frame_indexEnemyChica-1], (-(width * 0.11), height//3))
                        elif(state_battle_type == 3):
                            screen.blit(framesEnemyFoxy[frame_indexEnemyFoxy-1], (-(width * 0.11), height//2.35))

                elif(state_battle_type == 1):
                    if(counter_bonnie_attack_sound == 0):
                        channel_sound.play(bonnie_attack_sound)
                        counter_bonnie_attack_sound +=1
                    waitingEnemyAttack = -1
                    counter_chica_attack_sound = 0
                    counter_bonnie_attack_sound = 0
                    screen.blit(framesEnemyBonnie[frame_indexEnemyBonnie-1], (-(width * 0.08), height//3.5))
                elif(state_battle_type == 2):
                    if(counter_chica_attack_sound == 0):
                        channel_sound.play(chica_attack_sound)
                        counter_chica_attack_sound +=1
                    waitingEnemyAttack = -1
                    counter_chica_attack_sound = 0
                    counter_bonnie_attack_sound = 0
                    screen.blit(framesEnemyChica[frame_indexEnemyChica-1], (-(width * 0.11), height//3))
                elif(state_battle_type == 3):
                    if(counter_foxy_attack == 0):
                        hp_freddy -= 25
                        counter_foxy_attack +=1
                    waitingEnemyAttack = -1
                    counter_chica_attack_sound = 0
                    counter_bonnie_attack_sound = 0
                    counter_foxy_attack = 0
                    screen.blit(framesEnemyFoxy[frame_indexEnemyFoxy-1], (-(width * 0.11), height//2.35))
                elif(state_battle_type == 4):
                    waitingEnemyAttack = -1
                    counter_chica_attack_sound = 0
                    counter_bonnie_attack_sound = 0
                    counter_foxy_attack = 0
                    screen.blit(imageWordsGoldenFreddyBattle,imageWordsGoldenFreddyBattle_rect)
                    screen.blit(imageGoldenFreddyBattle,imageGoldenFreddyBattle_rect)
            else:
                if(current_hp <= 0 and not enterWinningBattle):
                    if(state_battle_type != 4):
                        if(counter_enemy_dead_sound == 0):
                            channel_music.play(enemy_dead_sound)
                            counter_enemy_dead_sound +=1
                        screen.blit(imageDeadEnemyIsOn,imageDeadEnemyIsOn_rect)
                    else:
                        defeat_final_enemy = True
                        waitingFinalEnemy = timeNow + 4000
                        gameVariables.isInitCombat = True 
                        gameVariables.isInitGameMap = True 
                elif(current_hp > 0):
                    if(state_battle_type == 0):
                        screen.blit(framesEnemyNormal[frame_indexEnemyNormal-1], (width//15, height//2.4))
                        pygame.time.delay(durationsEnemyNormal[frame_indexEnemyNormal-1])
                    elif(state_battle_type == 1):
                        screen.blit(framesEnemyBonnie[frame_indexEnemyBonnie-1], (-(width * 0.08), height//3.5))
                        pygame.time.delay(durationsEnemyBonnie[frame_indexEnemyBonnie-1])
                    elif(state_battle_type == 2):
                        screen.blit(framesEnemyChica[frame_indexEnemyChica-1], (-(width * 0.11), height//3))
                        pygame.time.delay(durationsEnemyChica[frame_indexEnemyChica-1])
                    elif(state_battle_type == 3):
                        screen.blit(framesEnemyFoxy[frame_indexEnemyFoxy-1], (-(width * 0.11), height//2.35))
                        pygame.time.delay(durationsEnemyFoxy[frame_indexEnemyFoxy-1])
                    elif(state_battle_type == 4):
                        screen.blit(imageGoldenFreddyBattle,imageGoldenFreddyBattle_rect)
                    
        if(enter_to_attack_freddy and waitingEnterToAttackFreddy != -1):
            elapsed_time = timeNow - waitingEnterToAttackFreddy
            if(attack_select_freddy == 1):
                if elapsed_time < 1000:
                    if(counter_sound_sprite1 == 0):
                        channel_sound_battle.play(freddy_attack_sprite_1)
                        counter_sound_sprite1 +=1
                    start_animation_attacks = False
                    waitingAnimationAttacksStart = -1
                    progress = elapsed_time / 1000
                    progress = min(progress, 1)
                    x_start = width // 2.1
                    x_end = width // 5
                    current_x = x_start + (x_end - x_start) * progress
                    current_y = height // 1.65
                    randomNumberAttack = random.randint(0, 2) 
                    if randomNumberAttack == 0:
                        screen.blit(imageFreddyAttackSprite1Part1, (current_x, current_y))
                    elif randomNumberAttack == 1:
                        screen.blit(imageFreddyAttackSprite1Part2, (current_x, current_y))
                    elif randomNumberAttack == 2:
                        screen.blit(imageFreddyAttackSprite1Part3, (current_x, current_y))
                else:
                    enter_to_attack_freddy = False
                    waitingEnterToAttackFreddy = -1
                    start_animation_attacks = True
                    waitingAnimationAttacksStart = 2000
                    audio_counter_sound_attacks_selection = 0
                    counter_sound_sprite1 = 0
    
            elif(attack_select_freddy == 2):
                if elapsed_time < 4000:
                    if(counter_sound_sprite2 == 0):
                        channel_sound_battle.play(freddy_attack_sprite_2)
                        counter_sound_sprite2 +=1
                    start_animation_attacks = False
                    waitingAnimationAttacksStart = -1
                    progress = elapsed_time / 4000
                    progress = min(progress, 1)
                    x_start_one = (width * 2) + (width * 0.3)
                    x_start_second = (width * 2) + (width * 1.4)
                    x_start_third = (width * 2) + (width * 2.7)
                    x_end = -width
                    current_x_firts = x_start_one + (x_end - x_start_one) * progress
                    current_x_second = x_start_second + (x_end - x_start_second) * progress
                    current_x_third = x_start_third + (x_end - x_start_third) * progress
                    randomNumberAttack = random.randint(0, 2) 
                    screen.blit(imageFreddyAttackSprite2, (current_x_firts, height// 1.8))
                    screen.blit(imageFreddyAttackSprite2, (current_x_second, height// 4))
                    screen.blit(imageFreddyAttackSprite2, (current_x_third, height// 15))
                else:
                    enter_to_attack_freddy = False
                    waitingEnterToAttackFreddy = -1
                    start_animation_attacks = True
                    waitingAnimationAttacksStart = 2000
                    audio_counter_sound_attacks_selection = 0
                    counter_sound_sprite2 = 0
            elif(attack_select_freddy == 3):
                if elapsed_time < 1500:
                    if(counter_sound_sprite3 == 0):
                        channel_sound_battle.play(freddy_attack_sprite_3)
                        counter_sound_sprite3 +=1
                        hp_freddy +=45
                    interval = 300  
                    current_phase = elapsed_time // interval  
                    phase_elapsed = elapsed_time % interval  
                    progress = phase_elapsed / interval  
                    if current_phase == 0:
                        screen.blit(imageFreddyAttackSprite3Part1,imageFreddyAttackSprite3Part1_rect)
                    elif current_phase == 1:
                        screen.blit(imageFreddyAttackSprite3Part2,imageFreddyAttackSprite3Part2_rect)
                    elif current_phase == 2:
                        screen.blit(imageFreddyAttackSprite3Part3,imageFreddyAttackSprite3Part3_rect)
                    elif current_phase == 3:
                        screen.blit(imageFreddyAttackSprite3Part4,imageFreddyAttackSprite3Part4_rect)
                    elif current_phase == 4:
                        screen.blit(imageFreddyAttackSprite3Part5,imageFreddyAttackSprite3Part5_rect)
                else:
                    enter_to_attack_freddy = False
                    waitingEnterToAttackFreddy = -1
                    start_animation_attacks = True
                    waitingAnimationAttacksStart = 2000
                    counter_sound_sprite3 = 0
                    audio_counter_sound_attacks_selection = 0
        if(enemy_is_in_attack and enemyIsInAttackWaiting != -1 and timeNow >= enemyIsInAttackWaiting):
            elapsed_time = timeNow - enemyIsInAttackWaiting
            if(attack_select_freddy == 1):
                if elapsed_time < 500:
                    if counter_enemy_damage_sound == 0:
                        channel_sound.play(enemy_damage_sound)
                        counter_enemy_damage_sound += 1
                        if(state_battle_type == 0):
                            hp_normal_enemy -= 15
                        elif(state_battle_type == 1):   
                            hp_bonnie -= 15
                        elif(state_battle_type == 2):
                            hp_chica -= 15
                        elif(state_battle_type == 3):
                            hp_foxy -= 15
                        elif(state_battle_type == 4):
                            hp_final_enemy -= 15
                        waitingWiningBattle = timeNow +  4000
                        on_punches_enemy = True
                        onPunchesEnemyWaiting = timeNow + 20
                        randomScenePunchEnemy = random.randint(0, 2)

                    progress = min(elapsed_time / 1000, 1)
                    start_x = width // 7.5
                    start_y = height // 2.25 
                    x_offset = width * 0.25           
                    end_y = height          
                    square_size = width * 0.03
                    left_x = start_x - (x_offset * progress)
                    right_x = start_x + (x_offset * progress)
                    current_y = start_y + ((end_y - start_y) * progress)  
                    square_left = pygame.Surface((square_size, square_size))
                    square_right = pygame.Surface((square_size, square_size))
                    square_left.fill((0, 0, 0))
                    square_right.fill((0, 0, 0))
                    screen.blit(square_left, (left_x, current_y))
                    screen.blit(square_right, (right_x, current_y))
                else:
                    enemy_is_in_attack = False
                    enemyIsInAttackWaiting = -1
                    counter_enemy_damage_sound = 0
            elif(attack_select_freddy == 2):
                if elapsed_time < 500:
                    if counter_enemy_damage_sound == 0:
                        channel_sound.play(enemy_damage_sound)
                        counter_enemy_damage_sound += 1
                        waitingWiningBattle = timeNow +  4000
                        if(state_battle_type == 0):
                            hp_normal_enemy -= 5
                        elif(state_battle_type == 1):   
                            hp_bonnie -= 5
                        elif(state_battle_type == 2):
                            hp_chica -= 5
                        elif(state_battle_type == 3):
                            hp_foxy -= 5
                        elif(state_battle_type == 4):
                            hp_final_enemy -= 5
                        on_punches_enemy = True
                        onPunchesEnemyWaiting = timeNow + 20
                        randomScenePunchEnemy = random.randint(0, 2)
                    progress = min(elapsed_time / 1000, 1)
                    start_x = width // 7.5
                    start_y = height // 2.25 
                    x_offset = width * 0.25           
                    end_y = height          
                    square_size = width * 0.03
                    left_x = start_x - (x_offset * progress)
                    right_x = start_x + (x_offset * progress)
                    current_y = start_y + ((end_y - start_y) * progress)  
                    square_left = pygame.Surface((square_size, square_size))
                    square_right = pygame.Surface((square_size, square_size))
                    square_left.fill((0, 0, 0))
                    square_right.fill((0, 0, 0))
                    screen.blit(square_left, (left_x, current_y))
                    screen.blit(square_right, (right_x, current_y))
                elif(elapsed_time < 700 and elapsed_time >= 500):
                    counter_enemy_damage_sound = 0
                elif(elapsed_time < 1300 and elapsed_time >= 700):
                    if counter_enemy_damage_sound == 0:
                        channel_sound.play(enemy_damage_sound)
                        counter_enemy_damage_sound += 1
                        if(state_battle_type == 0):
                            hp_normal_enemy -= 5
                        elif(state_battle_type == 1):   
                            hp_bonnie -= 5
                        elif(state_battle_type == 2):
                            hp_chica -= 5
                        elif(state_battle_type == 3):
                            hp_foxy -= 5
                        elif(state_battle_type == 4):
                            hp_final_enemy -= 5
                        waitingWiningBattle = timeNow +  4000
                        on_punches_enemy = True
                        onPunchesEnemyWaiting = timeNow + 20
                        randomScenePunchEnemy = random.randint(0, 2)
                    interval_elapsed = elapsed_time -700
                    progress = min(interval_elapsed / 1000, 1)
                    start_x = width // 7.5
                    start_y = height // 2.25 
                    x_offset = width * 0.25           
                    end_y = height          
                    square_size = width * 0.03
                    left_x = start_x - (x_offset * progress)
                    right_x = start_x + (x_offset * progress)
                    current_y = start_y + ((end_y - start_y) * progress)  
                    square_left = pygame.Surface((square_size, square_size))
                    square_right = pygame.Surface((square_size, square_size))
                    square_left.fill((0, 0, 0))
                    square_right.fill((0, 0, 0))
                    screen.blit(square_left, (left_x, current_y))
                    screen.blit(square_right, (right_x, current_y))
                elif(elapsed_time < 1500 and elapsed_time >= 1300):
                    counter_enemy_damage_sound = 0
                elif(elapsed_time < 2000 and elapsed_time >= 1500):
                    if counter_enemy_damage_sound == 0:
                        channel_sound.play(enemy_damage_sound)
                        counter_enemy_damage_sound += 1
                        if(state_battle_type == 0):
                            hp_normal_enemy -= 5
                        elif(state_battle_type == 1):   
                            hp_bonnie -= 5
                        elif(state_battle_type == 2):
                            hp_chica -= 5
                        elif(state_battle_type == 3):
                            hp_foxy -= 5
                        elif(state_battle_type == 4):
                            hp_final_enemy -= 5
                        waitingWiningBattle = timeNow + 4000
                        on_punches_enemy = True
                        onPunchesEnemyWaiting = timeNow + 20
                        randomScenePunchEnemy = random.randint(0, 2)
                    interval_elapsed = elapsed_time -1500
                    progress = min(interval_elapsed / 1000, 1)
                    start_x = width // 7.5
                    start_y = height // 2.25 
                    x_offset = width * 0.25           
                    end_y = height          
                    square_size = width * 0.03
                    left_x = start_x - (x_offset * progress)
                    right_x = start_x + (x_offset * progress)
                    current_y = start_y + ((end_y - start_y) * progress)  
                    square_left = pygame.Surface((square_size, square_size))
                    square_right = pygame.Surface((square_size, square_size))
                    square_left.fill((0, 0, 0))
                    square_right.fill((0, 0, 0))
                    screen.blit(square_left, (left_x, current_y))
                    screen.blit(square_right, (right_x, current_y))
                else:
                    enemy_is_in_attack = False
                    enemyIsInAttackWaiting = -1
                    counter_enemy_damage_sound = 0
        if(on_punches_enemy and onPunchesEnemyWaiting != -1):
            elapsed_time = timeNow - onPunchesEnemyWaiting
            if elapsed_time < 50:
                progress = elapsed_time / 50
                current_alpha = int(255 * progress)
                if(randomScenePunchEnemy == 0):
                    backgroundPunchEnemy1.set_alpha(current_alpha)
                    screen.blit(backgroundPunchEnemy1,(0,0))
                if(randomScenePunchEnemy == 1):
                    backgroundPunchEnemy2.set_alpha(current_alpha)
                    screen.blit(backgroundPunchEnemy2,(0,0))
                if(randomScenePunchEnemy == 2):
                    backgroundPunchEnemy3.set_alpha(current_alpha)
                    screen.blit(backgroundPunchEnemy3,(0,0))
            elif elapsed_time > 50 and elapsed_time < 100:
                progress = elapsed_time / 50
                current_alpha = int(255 * ( 1 - progress))
                if(randomScenePunchEnemy == 0):
                    backgroundPunchEnemy1.set_alpha(current_alpha)
                    screen.blit(backgroundPunchEnemy1,(0,0))
                if(randomScenePunchEnemy == 1):
                    backgroundPunchEnemy2.set_alpha(current_alpha)
                    screen.blit(backgroundPunchEnemy2,(0,0))
                if(randomScenePunchEnemy == 2):
                    backgroundPunchEnemy3.set_alpha(current_alpha)
                    screen.blit(backgroundPunchEnemy3,(0,0))
            else:
                on_punches_enemy = False
                onPunchesEnemyWaiting = -1
                randomScenePunchEnemy = 0
                backgroundPunchEnemy1.set_alpha(0)
                backgroundPunchEnemy2.set_alpha(0)
                backgroundPunchEnemy3.set_alpha(0)
        
        if(current_hp <= 0 and waitingWiningBattle != -1):
            elapsed_time = timeNow - waitingWiningBattle
            
            if elapsed_time > 0:
                if not enterWinningBattle:
                    enterWinningBattle = True
                    waitingExitBattle = timeNow + 7000
                randomPhotogram = random.randint(0, 2)  
                animation_duration = 1000  
                start_x = -imageWinningBattle1.get_width()  
                end_x = width // 6
                y_pos = height // 14

                if elapsed_time < animation_duration:
                    progress = elapsed_time / animation_duration
                    current_x = start_x + (end_x - start_x) * progress
                else:
                    current_x = end_x  
                if randomPhotogram == 0:
                    screen.blit(imageWinningBattle1, (current_x, y_pos))
                elif randomPhotogram == 1:
                    screen.blit(imageWinningBattle2, (current_x, y_pos))
                elif randomPhotogram == 2:
                    screen.blit(imageWinningBattle3, (current_x, y_pos))
            if(enterWinningBattle and waitingExitBattle != -1 and timeNow >= waitingExitBattle):
                gameVariables.isInitCombat = True 
                gameVariables.isInitGameMap = False 
                waitingEnemyPosition = -1
                waitingEnemyPosition = -1
                start_animation_attacks = False
                end_animation_attacks = False
                audio_counter_sound_attacks_selection = 0
                waitingAnimationAttacksStart = -1
                waitingAnimationAttacksEnd = -1
                waitingEnemyAttack = -1
                waitingReapearAttacksFreddy = -1
                attack_select_freddy = 0
                animate_freddy_attack = False
                animate_freddy_attack_waiting = -1
                enter_to_attack_freddy = False
                waitingEnterToAttackFreddy = -1
                enemy_is_in_attack = False
                on_punches_enemy = False
                enemyIsInAttackWaiting = -1
                onPunchesEnemyWaiting = -1
                randomScenePunchEnemy = 0
                waitingWiningBattle = -1
                enterWinningBattle = False
                waitingExitBattle = -1
                counter_enemy_dead_sound = 0
                hp_freddy = 100
                hp_normal_enemy = 50
                if(state_battle_type == 1):
                    hp_bonnie = 0
                    defeat_bonnie = True
                elif(state_battle_type == 2):
                    hp_chica = 0
                    defeat_chica = True
                if(state_battle_type == 3):
                    hp_foxy = 0
                    defeat_foxy = True
                hp_foxy = 300
        
        pygame.display.flip()
    if(gameVariables.isInitShopMangle and gameVariables.isInitCombat and gameVariables.isInitGameMap):
        if(counterMusicMap == 1):
            channel_music.stop()
        screen.fill((0,0,0))
        screen.blit(backgroundMangleShop,(0,0))
        screen.blit(imageMangleInShop,imageMangleInShop_rect)
        screen.blit(imageFreddyStatic,imageFreddyStatic_rect)
        screen.blit(imageButtonBackShop,imageButtonBackShop_rect)
        if(not masc_freddy_shop):
            screen.blit(imageFreddyMask,imageFreddyMask_rect)
        pygame.display.flip()
    if(gameVariables.isInitShopBallonGirl and gameVariables.isInitCombat and gameVariables.isInitGameMap and waitingBackgroundBallonGirl != -1):
        elapsed_time = timeNow - waitingBackgroundBallonGirl
        screen.fill((0,0,0))
        if(counterMusicMap == 1):
            channel_music.stop()
        if elapsed_time > 0:
            screen.blit(backgroundBallonGirlShop,(0,0))
        screen.blit(imageBallonGirlInShop,imageBallonGirlInShop_rect)
        if(not unlock_padlock):
            screen.blit(imageButtonPlay,imageButtonPlay_rect)
        screen.blit(imageFreddyStatic,imageFreddyStatic_rect)
        screen.blit(imageButtonBackShop,imageButtonBackShop_rect)
        pygame.display.flip()
    if(gameVariables.isInitMiniGameBallonGirl and gameVariables.isInitCombat and gameVariables.isInitGameMap):
        if(counter_background_mini_game_ballon_girl_music == 0):
            channel_music.play(background_mini_game_ballon_girl_music,loops=-1)
            counter_background_mini_game_ballon_girl_music = 1
        speed = width * 0.0025
        left_limit = 0
        right_limit = width - (imageHeartMiniGameBallonGirl.get_width() * 2.5)  

        if type_movement_heart == 1: 
            if movement_heart_mini_game_x - speed <= left_limit:
                movement_heart_mini_game_x = left_limit
                type_movement_heart = 2
            else:
                movement_heart_mini_game_x -= speed

        elif type_movement_heart == 2:  
            if movement_heart_mini_game_x + speed >= right_limit:
                movement_heart_mini_game_x = right_limit
                type_movement_heart = 1
            else:
                movement_heart_mini_game_x += speed
        screen.fill((0,0,0))
        screen.blit(backgroundMiniGameBallonGirl,(0,0))
        screen.blit(imageFreedbearMiniGameBallonGirl,(imageFreedbearMiniGameBallonGirl_rect.x + movement_freedbear_mini_game_x,imageFreedbearMiniGameBallonGirl_rect.y))
        screen.blit(imageHeartMiniGameBallonGirl,(movement_heart_mini_game_x,imageHeartMiniGameBallonGirl_rect.y))
        if(waitingWordsCompleteMiniGame != -1):
            elapsed_time = timeNow - waitingWordsCompleteMiniGame
            if elapsed_time > 0:
                screen.blit(imageWinningMiniGameBallonGirl,imageWinningMiniGameBallonGirl_rect)
            if elapsed_time > 4000:
                gameVariables.isInitShopMangle = False
                gameVariables.isInitShopBallonGirl = False
                gameVariables.isInitMiniGameBallonGirl = False
                gameVariables.isInitCombat = True 
                gameVariables.isInitGameMap = False
                counterMusicMap = 0
                
        pygame.display.flip()
    if(waitingEnterFinalBattle != -1 and state_battle_type != 4):
        gameVariables.isInitCombat = False
        gameVariables.isInitGameMap = True
        waitingEnemyPosition = timeNow + 200
        state_battle_type = 4
        channel_music.stop()
        counterMusicMap = 0
    if(defeat_final_enemy and waitingFinalEnemy != -1 and gameVariables.isInitCombat and gameVariables.isInitGameMap and not winning_game):
        elapsed_time = timeNow - waitingFinalEnemy
        if elapsed_time < 0:
            channel_music.stop()
            screen.fill((255,255,255))
        elif elapsed_time > 0 and elapsed_time < 4000:
            if(counter_winning_game_music == 0):
                channel_music.play(winning_game_music)
                counter_winning_game_music +=1
            randomNumber = random.randint(0, 1)
            screen.blit(background_winning_game,(0,0))
            if(randomNumber == 0):
                screen.blit(imageWinningWordsPart1,imageWinningWordsPart1_rect)
            elif(randomNumber == 1):    
                screen.blit(imageWinningWordsPart2,imageWinningWordsPart2_rect)
        elif(elapsed_time > 4000 and elapsed_time < 5500):
            screen.blit(background_winning_game,(0,0))
            screen.blit(imageWinningWordsPart1,imageWinningWordsPart1_rect)
        elif(elapsed_time > 5500 and elapsed_time < 6000):
            channel_music.stop()
            screen.blit(background_winning_game,(0,0))
            screen.blit(imageWinningWordsPart1,imageWinningWordsPart1_rect)
            screen.blit(imageWinningFreedbear,imageWinningFreedbear_rect)
            winning_game = True
        pygame.display.flip()
    if(winning_game):
        if(counter_winning__counter_music == 0):
            channel_music.play(winning_counter_music,loops=-1)
            counter_winning__counter_music +=1
        screen.fill((0,0,0))
        screen.blit(background_winning_counter,(0,0)) 
        if(waitingCounterSeconds == -1):
            waitingCounterSeconds = timeNow + 1000
        else:
            if(timeNow >= waitingCounterSeconds):
                counterLastTime -= 1
                waitingCounterSeconds = -1
        if(frame_indexFredyCounter >= len(framesFredyCounter)):
            frame_indexFredyCounter = 0
        else:
            frame_indexFredyCounter +=1
        if(counterLastTime <= 0):
            running = False
            show_message_developer = True
        counter_text = font.render(f"00:{counterLastTime}", True, (255, 255, 255))
        screen.blit(counter_text, (width//1.5, height//1.35))
        screen.blit(framesFredyCounter[frame_indexFredyCounter-1], (width // 600, height//2.05))
        pygame.time.delay(durationsFredyCounter[frame_indexFredyCounter-1])
        
        pygame.display.flip()
    if(hp_freddy <= 0 ):
        if(counter_game_over == 0):
            channel_music.stop()
            channel_sound.stop()
            channel_sound_battle.stop()
            channel_music.play(game_over)
            waitingGameOver = timeNow + 6000
            gameVariables.isInitCombat = True 
            gameVariables.isInitGameMap = True 
            counter_game_over +=1
        if(waitingGameOver != -1):
            if(timeNow>= waitingGameOver):
                gameVariables.isInitCombat = True 
                gameVariables.isInitGameMap = False 
                waitingEnemyPosition = -1
                waitingEnemyPosition = -1
                start_animation_attacks = False
                end_animation_attacks = False
                audio_counter_sound_attacks_selection = 0
                waitingAnimationAttacksStart = -1
                waitingAnimationAttacksEnd = -1
                waitingEnemyAttack = -1
                waitingReapearAttacksFreddy = -1
                attack_select_freddy = 0
                animate_freddy_attack = False
                animate_freddy_attack_waiting = -1
                counter_bonnie_battle_music = 0
                enter_to_attack_freddy = False
                waitingEnterToAttackFreddy = -1
                enemy_is_in_attack = False
                on_punches_enemy = False
                enemyIsInAttackWaiting = -1
                onPunchesEnemyWaiting = -1
                randomScenePunchEnemy = 0
                waitingWiningBattle = -1
                enterWinningBattle = False
                waitingExitBattle = -1
                counter_enemy_dead_sound = 0
                hp_freddy = 100
                hp_normal_enemy = 50
        screen.fill((0,0,0))
        screen.blit(backgroundGameOver,(0,0))
        pygame.display.flip()
        pygame.time.delay(100)
if show_message_developer:
    ctypes.windll.user32.MessageBoxW(0, "¡You Have Been Hacked!", "Све ваше информације cy украдене и успешно архивиране", 0x40 | 0x1)
    ctypes.windll.user32.MessageBoxW(0, "¡It's a joke!//¡Es Broma!", "Developed by César Vielmas // Desarrollado Por César Vielmas", 0x40 | 0x1)
pygame.quit()
