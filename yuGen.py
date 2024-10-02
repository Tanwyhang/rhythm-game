import os
from configparser import ConfigParser
import pygame
import sys
import json
import random

# colors

pygame.mixer.init(buffer=512)
pygame.mixer.set_num_channels(10000)

pygame.init()

pygame.display.set_caption('yuGen')
icon = pygame.image.load('yuGen_data\\skin\\yugenlogo.png')
pygame.display.set_icon(icon)
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
width = monitor_size[0]
height = monitor_size[1]
width_middle = width / 2

# scaling

screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN + pygame.DOUBLEBUF)
scale_width = (width / 1536)
scale_height = (height / 864)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 223, 0)

# reading settings

settings_file = os.path.join('yuGen_data', 'skin', 'settings.ini')
config = ConfigParser()
config.read(settings_file)

# settings variable

FPS = int(config['performance']['fps'])
speed = 150
main_menu_background_brightness = int(config['effects']['main menu background brightness'])
song_selection_background_brightness = int(config['effects']['song selection background brightness'])


logo_size = float(config['appearance']['logo size'])
menu_icon_size = float(config['appearance']['menu icon size'])
song_cover_size = float(config['appearance']['song cover size'])

parallax_enabled = config['performance']['parallax background']
background_animation = config['performance']['background animation']

menu_music_play = config['audio']['menu_music']

run_music = 0
logo_alpha = 0
bg_alpha = 0

pygame.mouse.set_visible(False)

difficulty_selection = 2
line_width = 10 * scale_height
song_current_select = 0
difficulty_alpha = 0
clock = pygame.time.Clock()

total_images = 0
for i in range(1, 999):
    if os.path.isfile(f'yuGen_data\\skin\\menu-bg({i}).jpg'):
        total_images = i
    else:
        break


mouse_x, mouse_y = pygame.mouse.get_pos()

# font

font_name = os.path.join('yuGen_data', 'skin', 'font.TTF')
font_big = pygame.font.Font(font_name, int(height / 27))
font_large = pygame.font.Font(font_name, int(height / 21))
font = pygame.font.Font(font_name, int(height / 54))


def draw_text(surf, text, pos_x, pos_y, size=None):

    if size == 'big':

        text_surface = font_big.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topleft = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    elif size == 'large':

        text_surface = font_large.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topleft = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    else:

        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topleft = pos_x, pos_y
        surf.blit(text_surface, text_rect)


def draw_text_rgb(surf, text, color, pos_x, pos_y, size=None):

    if size == 'big':

        text_surface = font_big.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    elif size == 'large':

        text_surface = font_large.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    else:

        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = pos_x, pos_y
        surf.blit(text_surface, text_rect)


def draw_text_centered_gold(surf, text, pos_x, pos_y, size=None):

    if size == 'big':

        text_surface = font_big.render(text, True, GOLD)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    elif size == 'large':

        text_surface = font_large.render(text, True, GOLD)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    else:

        text_surface = font.render(text, True, GOLD)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)


def draw_text_centered_rgb(surf, text, color, pos_x, pos_y, size=None):

    if size == 'big':

        text_surface = font_big.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    elif size == 'large':

        text_surface = font_large.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    else:

        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)


def draw_text_centered(surf, text, pos_x, pos_y, size=None):

    if size == 'big':

        text_surface = font_big.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    elif size == 'large':

        text_surface = font_large.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    else:

        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)


def draw_text_centered_alpha(surf, text, pos_x, pos_y, size=None, alpha=100):

    if size == 'big':

        text_surface = font_big.render(text, True, WHITE)
        text_surface.set_alpha(alpha)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    elif size == 'large':

        text_surface = font_large.render(text, True, WHITE).set_alpha(alpha)
        text_surface.set_alpha(alpha)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)

    else:

        text_surface = font.render(text, True, WHITE).set_alpha(alpha)
        text_surface.set_alpha(alpha)
        text_rect = text_surface.get_rect()
        text_rect.center = pos_x, pos_y
        surf.blit(text_surface, text_rect)


# sfx

menu_music = os.path.join('yuGen_data', 'skin', 'sound-menu_theme.mp3')
hit_sound = pygame.mixer.Sound(os.path.join('yuGen_data', 'skin', 'sound-hit.wav'))
intro_sound = pygame.mixer.Sound(os.path.join('yuGen_data', 'skin', 'sound-intro.wav'))
enter_sound = pygame.mixer.Sound(os.path.join('yuGen_data', 'skin', 'sound-enter.wav'))
back_sound = pygame.mixer.Sound(os.path.join('yuGen_data', 'skin', 'sound-back.wav'))
select_sound = pygame.mixer.Sound(os.path.join('yuGen_data', 'skin', 'sound-select.wav'))
hover_sound = pygame.mixer.Sound(os.path.join('yuGen_data', 'skin', 'sound-hover.wav'))
start_sound = pygame.mixer.Sound(os.path.join('yuGen_data', 'skin', 'sound-play.wav'))
hit_sound.set_volume(1)
enter_sound.set_volume(0.7)
back_sound.set_volume(0.7)

# image

frame_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'menu-frame.png')).convert_alpha()
frame_pic = pygame.transform.scale(frame_pic,
                                   (width * 0.5 * song_cover_size, height * 0.5 * song_cover_size)).convert_alpha()
frame_pic_v = pygame.image.load(os.path.join('yuGen_data', 'skin', 'menu-frame-V.png')).convert_alpha()
frame_pic_v = pygame.transform.scale(frame_pic_v,
                                     (width * 0.5 * song_cover_size, height * 0.5 * song_cover_size)).convert_alpha()

enter_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'menu_enter_button.png')).convert_alpha()
settings_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'menu_setting_button.png')).convert_alpha()
back_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'menu_back_button.png')).convert_alpha()

hit_circle_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'game-hitcircle.png')).convert_alpha()
hit_circle_pic = pygame.transform.smoothscale(hit_circle_pic, (128 * scale_width, 128 * scale_height)).convert_alpha()
hit_circle_size = [hit_circle_pic.get_rect()[2], hit_circle_pic.get_rect()[3]]
circle_radius = hit_circle_size[0] / 2

scanner_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'game-scanner.png')).convert_alpha()
scanner_pic = pygame.transform.smoothscale(scanner_pic, (105 * scale_width, 105 * scale_height)).convert_alpha()

scanner_size = [scanner_pic.get_rect()[2], scanner_pic.get_rect()[3]]
scanner_radius = scanner_size[0] / 2

round_corner_square_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'game-square.png')).convert_alpha()

rank_V_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'rank-V.png')).convert_alpha()
rank_S_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'rank-S.png')).convert_alpha()
rank_A_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'rank-A.png')).convert_alpha()
rank_B_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'rank-B.png')).convert_alpha()
rank_C_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'rank-C.png')).convert_alpha()
rank_F_pic = pygame.image.load(os.path.join('yuGen_data', 'skin', 'rank-F.png')).convert_alpha()


rank_V_pic = pygame.transform.smoothscale(rank_V_pic, [height / 1.5, height / 1.5])
rank_S_pic = pygame.transform.smoothscale(rank_S_pic, [height / 1.5, height / 1.5])
rank_A_pic = pygame.transform.smoothscale(rank_A_pic, [height / 1.5, height / 1.5])
rank_B_pic = pygame.transform.smoothscale(rank_B_pic, [height / 1.5, height / 1.5])
rank_C_pic = pygame.transform.smoothscale(rank_C_pic, [height / 1.5, height / 1.5])
rank_F_pic = pygame.transform.smoothscale(rank_F_pic, [height / 1.5, height / 1.5])

rank_image_radius = rank_A_pic.get_rect()[3] / 2

circle_surf = pygame.Surface((hit_circle_size[0], hit_circle_size[1]))
scanner_surf = pygame.Surface((scanner_size[0], scanner_size[1]))

circle_surf.blit(hit_circle_pic, (0, 0))
circle_surf.set_colorkey(BLACK)

scanner_surf.blit(scanner_pic, (0, 0))
scanner_surf.set_colorkey(BLACK)

# songs

songs_files = os.listdir('yuGen_data/songs')
songs_count = len(songs_files)

cover = 0
audio = 1
beatmap = 2
high_score = 3
beatmap_path = 4
play_time = 5

song_list = []
songs_loaded = 0


def load_songs():

    global songs_loaded

    for songs in songs_files:

        screen.fill(BLACK)
        draw_text(screen, f'loading easy songs... {songs_loaded + 1} / {songs_count}', 0, 0, 'big')
        draw_text(screen, f'loaded: {songs}', 0, 55)
        pygame.display.flip()

        data_ = open(f"yuGen_data\\songs\\{songs}\\beatmap.json", 'r')
        data = json.load(data_)
        song_score = int(data["score"])
        timing = int(data['menu-play'])
        song_map = data["hitobjects"]

        song_list.append([pygame.image.load(os.path.join('yuGen_data', 'songs', songs, 'cover.jpg')), (
            os.path.join('yuGen_data', 'songs', songs, 'audio.mp3')),
            song_map,
            song_score,
            f"yuGen_data\\songs\\{songs}\\beatmap.json",
            timing])

        songs_loaded = len(song_list)
        data_.close()
        data = None


# batch load

main_menu_bg = []

load_songs()

if total_images > 1 and background_animation == 'True':

    for x in range(1, total_images):

        # no. of frames

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        frame = pygame.image.load(os.path.join('yuGen_data', 'skin', f'menu-bg({x}).jpg')).convert()
        if config['appearance']['background_blur'] == 'True':

            frame = pygame.transform.smoothscale(frame, (width * 0.05,
                                                 height * 0.05)).convert()

        frame = pygame.transform.smoothscale(frame, (width * 1.1,
                                                     height * 1.1
                                                     )).convert()
        frame.set_alpha(100)
        main_menu_bg.append(frame)
        check = x - 1
        i = x

        pygame.display.flip()
        screen.fill(BLACK)
        draw_text(screen, f'loading assets...{int((i / total_images) * 100)}%', 0, 0, 'big')

else:

    frame = pygame.image.load(os.path.join('yuGen_data', 'main_menu_background', f'menu-bg({1}).jpg')).convert()
    frame = pygame.transform.smoothscale(frame, (width * 1.1, height * 1.1)).convert()
    frame.set_alpha(100)
    main_menu_bg.append(frame)
    check = 0
    i = 1


# Classes


class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # importing data
        self.main_menu_bg = main_menu_bg
        self.check = check

        # general settings
        self.width = width
        self.height = height
        self.frame = i
        self.alpha = 100
        self.modifier = 0
        self.snap_frame = int(self.frame)
        self.image = self.main_menu_bg[0]
        self.rect = self.image.get_rect()
        self.rect.center = [width / 2, height / 2]
        self.pos_x = width / 2
        self.pos_y = height / 2

        # effects

    def alt_update(self):

        if total_images > 1 and background_animation == 'True':

            if self.frame >= self.check:
                self.frame = 0
            self.snap_frame = int(self.frame)
            self.image = self.main_menu_bg[int(self.snap_frame)]
            self.frame += 0.2 * dt

        if parallax_enabled == 'True':
            self.target_pos = [mouse_x * -0.02 * scale_width + self.rect[2] * 0.45,
                               mouse_y * -0.01 * scale_height + self.rect[3] * 0.45]
            self.pos_x += ((self.target_pos[0] - self.pos_x) * 0.1) * dt
            self.pos_y += ((self.target_pos[1] - self.pos_y) * 0.3) * dt
            self.rect.center = [self.pos_x, self.pos_y]

        if run:
            self.image.set_alpha(main_menu_background_brightness)
        if run_song_selection:
            self.image.set_alpha(song_selection_background_brightness)


class Logo(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # importing data
        self.width = height * logo_size
        self.height = height * logo_size
        self.logo = pygame.image.load(os.path.join('yuGen_data', 'skin', 'logo.png')).convert_alpha()
        self.logo = pygame.transform.smoothscale(self.logo, (self.width, self.height))

        # general settings

        self.image = self.logo
        self.rect = self.image.get_rect()
        self.rect.center = [width / 2, height / 2.3]
        self.image.set_alpha(0)
        self.pos_x = width / 2
        self.pos_y = height / 2

    def update(self):

        if parallax_enabled == 'True':

            self.target_pos = [mouse_x * -0.03 + width * 0.515,
                               mouse_y * -0.03 + height * 0.515]
            self.pos_x += ((self.target_pos[0] - self.pos_x) * 0.1) * dt
            self.pos_y += ((self.target_pos[1] - self.pos_y) * 0.1) * dt
            self.rect.center = [self.pos_x, self.pos_y - height / 15]

        draw_text(screen, 'programmed by @SeniorOne/Tanwyhang', 0, height * 0.97)


class Enter_button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # importing data

        self.image_base = enter_pic
        self.width = width / 4.75 * 0.8
        self.height = height / 7 * 0.8
        self.hover = False
        self.ready_to_press = False
        self.image_small = pygame.transform.scale(self.image_base, (self.width, self.height)).convert_alpha()
        self.image_big = pygame.transform.scale(self.image_base, (self.width * 1.1, self.height * 1.1)).convert_alpha()

        self.image = self.image_small

        # general settings
        self.rect = self.image.get_rect()
        self.rect.center = [width * 0.973, height * 0.045]
        self.pos_x = width / 2
        self.pos_y = height / 2

        self.image.set_alpha(255)

    def update(self):

        if parallax_enabled == 'True':
            self.target_pos = [mouse_x * -0.03 + width * 0.515,
                               mouse_y * -0.03 + height * 0.515]
            self.pos_x += ((self.target_pos[0] - self.pos_x) * 0.1) * dt
            self.pos_y += ((self.target_pos[1] - self.pos_y) * 0.1) * dt
            self.rect.center = [self.pos_x, self.pos_y + (height / 6)]

            if detect_button(self):
                self.image = self.image_big
                self.ready_to_press = True
                if not self.hover:
                    hover_sound.play()
                    self.hover = True
            else:
                self.image = self.image_small
                self.hover = False
                self.ready_to_press = False


class Setting_button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # importing data

        self.image_base = settings_pic
        self.width = width / 4.75 * 0.8
        self.height = height / 7 * 0.8
        self.hover = False
        self.ready_to_press = False
        self.image_small = pygame.transform.scale(self.image_base, (self.width, self.height)).convert_alpha()
        self.image_big = pygame.transform.scale(self.image_base, (self.width * 1.2, self.height * 1.2)).convert_alpha()
        self.pos_x = width / 2 + width
        self.pos_y = height / 2

        self.image = self.image_small

        # general settings
        self.rect = self.image.get_rect()

        self.image.set_alpha(255)

    def update(self):

        if parallax_enabled == 'True':
            self.target_pos = [mouse_x * -0.03 + width * 0.515,
                               mouse_y * -0.03 + height * 0.515]
            self.pos_x += ((self.target_pos[0] - self.pos_x) * 0.1) * dt
            self.pos_y += ((self.target_pos[1] - self.pos_y) * 0.1) * dt
            self.rect.center = [self.pos_x, self.pos_y + (height / 3.5)]

        if detect_button(self):
            self.image = self.image_big
            self.ready_to_press = True
            if not self.hover:
                hover_sound.play()
                self.hover = True
        else:
            self.image = self.image_small
            self.hover = False
            self.ready_to_press = False


class Back_button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # importing data

        self.image_base = back_pic
        self.width = width / 4.75 * 0.8
        self.height = height / 7 * 0.8
        self.hover = False
        self.ready_to_press = False
        self.image_small = pygame.transform.scale(self.image_base, (self.width, self.height)).convert_alpha()
        self.image_big = pygame.transform.scale(self.image_base, (self.width * 1.1, self.height * 1.1)).convert_alpha()

        # general settings
        self.image = self.image_small
        self.image.set_alpha(255)

        # general settings
        self.rect = self.image.get_rect()
        self.rect.center = [width * 0.973, height * 0.045]

    def update(self):

        self.rect.center = [width * 0.1, height * 0.9]

        if detect_button(self):
            self.ready_to_press = True
            self.image = self.image_big
            if not self.hover:
                hover_sound.play()
                self.hover = True
        else:
            self.image = self.image_small
            self.hover = False
            self.ready_to_press = False


class Songs(pygame.sprite.Sprite):

    def __init__(self, image, sep):
        super().__init__()

        # cover settings

        self.pos_x = width / 2
        self.pos_y = height / 2
        self.image = image
        self.width = width
        self.height = height
        self.sep = sep

        self.image = pygame.transform.scale(self.image,
                                            (width / 2 * song_cover_size,
                                             height / 2 * song_cover_size)).convert()
        self.frame_image = frame_pic
        self.frame_image_v = frame_pic_v
        self.frame_rect = self.frame_image.get_rect()
        self.pos_x = self.pos_x + (width * sep)
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y - height]
        self.image.set_alpha(255)

    def update(self):
        self.score = song_list[self.sep][high_score]
        self.rect.center = [self.pos_x, self.pos_y]

        if self.score == 1_000_000:
            screen.blit(self.frame_image_v, (self.pos_x - self.frame_rect[2] / 2, self.pos_y - self.frame_rect[3] / 2))
        else:
            screen.blit(self.frame_image, (self.pos_x - self.frame_rect[2] / 2, self.pos_y - self.frame_rect[3] / 2))

        draw_text_centered(screen, songs_files[self.sep], self.pos_x, self.pos_y + height / 3, 'big')
        draw_text_centered_rgb(screen, f'HighScore: {str(self.score)}',
                               (255, 223, 255 - 255 * self.score / 1_000_000),
                               self.pos_x, self.pos_y - height / 3, 'big')
        alpha_smooth_transform_add(self, self.image.get_alpha() + 1, 150)
        smooth_transform_pos_y(self, height / 2)
        if self.sep == 0:
            draw_text_centered(screen, 'D', self.pos_x + width / 3, self.pos_y, 'big')
        elif self.sep == len(song_list) - 1:
            draw_text_centered(screen, 'A', self.pos_x - width / 3, self.pos_y, 'big')
        else:
            draw_text_centered(screen, 'D', self.pos_x + width / 3, self.pos_y, 'big')
            draw_text_centered(screen, 'A', self.pos_x - width / 3, self.pos_y, 'big')


class Hit:

    def __init__(self, pos):
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        self.pos = (pos[0], pos[1])
        self.size = circle_size / 2
        self.width = 8 * scale_height
        self.particles = []
        for i in range(3 + round(bps_value / 3)):
            self.particles.append([[random.randint(int(pos[0]), int(pos[0])),
                                   random.randint(int(pos[1]), int(pos[1]))],
                                   [random.randint(int(-width / 500), int(width / 500)),
                                   [height * 0.01, height * -0.02]],
                                  random.randint(int(width * 0.001), int(width * 0.005))])

    def update(self):
        if self.width > 1:
            pygame.draw.circle(screen, WHITE, self.pos, self.size, abs(int(self.width)))
            if self.size < 80 * scale_width:
                self.size += (1 + (self.size * 0.05)) * dt
            self.width -= 0.5 * dt
        for i in self.particles:
            i[0][0] += i[1][0] * dt
            i[0][1] += (i[1][1][1] + i[1][1][0]) * dt
            i[1][1][1] += height / 2000 * dt
            i[2] -= height / 20000 * dt
            if i[2] <= 0:
                self.particles.remove(i)
            pygame.draw.circle(screen, WHITE, [i[0][0], i[0][1]], i[2])


class Miss:

    def __init__(self, pos):

        self.pos = (pos[0], pos[1])
        self.size = circle_size / 2
        self.width = 8 * scale_height

    def update(self):
        if self.width > 1:
            pygame.draw.circle(screen, RED, self.pos, self.size, abs(int(self.width)))
            if self.size < 80 * scale_width:
                self.size += 1 + (1 + (self.size * 0.05)) * dt
            self.width -= 0.5 * dt


class Circle:

    def __init__(self, pos, time):
        super().__init__()

        self.time = time
        self.pos = pos
        self.alpha = 0
        self.surf = circle_surf.copy()
        self.can_press = False

    def update(self):

        self.surf.set_alpha(self.alpha)
        screen.blit(self.surf, (self.pos[0] - (hit_circle_size[0] / 2), self.pos[1] - (hit_circle_size[1] / 2)))

        if elapsed_time > (self.time + hit_window):
            self.surf.set_alpha(0)
            hit_effects.append(Miss(circle_objects[0].pos))
            circle_objects.pop(0)
            game.combo = 0
            game.misses += 1
            game.passed += 1

        if elapsed_time >= (self.time - hit_window):
            self.can_press = True
            if self.alpha < 200:
                self.modifier = abs((255 - self.alpha)) / 50
                self.alpha += 5 * self.modifier * dt

        if self.alpha < 100:
            self.alpha += 1 * dt


class Scanner:

    def __init__(self):
        super().__init__()
        self.surf = scanner_surf.copy()
        self.rect = scanner_size
        self.alpha = 0
        self.pos = [width / 2, height / 2]

    def update(self):

        if len(circle_objects_for_scanner) > 0 and elapsed_time > circle_objects_for_scanner[0][1]:
            circle_objects_for_scanner.pop(0)
            if guide.checkpoint % 2 == 0:
                guide.alpha = 255
            else:
                guide.alpha_2 = 255
            guide.checkpoint += 1

        if len(circle_objects_for_scanner) > 0:
            mod = abs(circle_objects_for_scanner[0][1] - (elapsed_time)) / 10 + 1
            dx = (circle_objects_for_scanner[0][0][0] - self.pos[0])
            dy = (circle_objects_for_scanner[0][0][1] - self.pos[1])
            self.pos[0] += ((dx / mod) * 3) * dt
            self.pos[1] += ((dy / mod * 5)) * dt
            if self.alpha < 255:
                self.alpha += 5 * dt

        else:
            self.alpha = 0

        self.surf.set_alpha(self.alpha)
        screen.blit(self.surf, (self.pos[0] - (self.rect[0] / 2), self.pos[1] - (self.rect[1] / 2)))


class Guide:

    def __init__(self):
        super().__init__()
        self.image = round_corner_square_pic
        self.image = pygame.transform.scale(self.image, (80 * scale_width, 80 * scale_height)).convert()
        self.rect = self.image.get_rect()
        self.surf = pygame.Surface((self.rect[2], self.rect[3])).convert()
        self.surf.set_colorkey(BLACK)
        self.surf_2 = pygame.Surface((self.rect[2], self.rect[3])).convert()
        self.surf_2.set_colorkey(BLACK)
        self.alpha = 0
        self.alpha_2 = 0
        self.pos = [monitor_size[0] / 2, monitor_size[1] / 2]
        self.checkpoint = 0

    def update(self):

        self.surf.set_alpha(self.alpha)
        self.surf_2.set_alpha(self.alpha_2)

        self.surf.blit(self.image, (0, 0))
        self.surf_2.blit(self.image, (0, 0))

        screen.blit(self.surf, (width * 0.87, height * 0.06))
        screen.blit(self.surf_2, (width * 0.94, height * 0.06))

        self.alpha -= 20 * dt
        self.alpha_2 -= 20 * dt


class Game:
    def __init__(self):
        self.passed = 0
        self.combo = 0
        self.misses = 0
        self.bad = 0
        self.hits = 0
        self.accuracy = 100
        self.surf = pygame.Surface(monitor_size)

    def judge_rank(self, score):

        rank_image = None
        if score != 1_000_000:
            if score >= 700_000:
                rank_image = rank_C_pic
            if score >= 800_000:
                rank_image = rank_B_pic
            if score >= 900_000:
                rank_image = rank_A_pic
            if score >= 950_000:
                rank_image = rank_S_pic
        else:
            rank_image = rank_V_pic

        if score < 700_000:
            rank_image = rank_F_pic

        return rank_image


# effect/scene functions

def check_close():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()


def draw_cursor():
    '''
    draw_text_centered(screen, f'pos_x: {round(mouse_x / width * 100)}% pos_y: {round(mouse_y / height * 100)}%',
                       mouse_x + width / 4 - (mouse_x * 0.5 - width * 0.05),
                       mouse_y + height / 4 - (mouse_y * 0.5 - height * 0.1))

    pygame.draw.line(screen, WHITE, (mouse_x, mouse_y),
                     (mouse_x + width / 4 - (mouse_x * 0.5 - width * 0.05),
                      mouse_y + height / 4 - (mouse_y * 0.5 - height * 0.1)), 3)

    pygame.draw.line(screen, WHITE, [mouse_x, 0], [mouse_x, height], 3)
    pygame.draw.line(screen, WHITE, [0, mouse_y], [width, mouse_y], 3)
'''

    pygame.draw.circle(screen, WHITE, [mouse_x, mouse_y], int(7 * scale_width))


def fade_in():

    global mouse_x, mouse_y, last_frame, dt
    fade = pygame.Surface((width, height))
    fade.fill(BLACK)

    fade.set_alpha(0)
    alpha = 100
    while True:
        if alpha < 255:
            dt = pygame.time.get_ticks() - last_frame
            dt = delta_to_modifier(dt)
            last_frame = pygame.time.get_ticks()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_close()
            screen.fill(BLACK)
            screen.blit(bg.image, [bg.rect.center[0] - width / 2, bg.rect.center[1] - height / 2])
            sprite.draw(screen)
            bg.alt_update()
            draw_cursor()
            sprite.update()
            draw_text(screen, f'FPS: {int(fps)}/{str(FPS)}', 10, 0, 'big')
            ######################
            fade.set_alpha(alpha)
            screen.blit(fade, (0, 0))
            ######################
            song_selection_updater()
            detect_button(song_selection[song_current_select])
            pygame.display.update()
            alpha += 10 * dt
        else:
            break


def fade_out():
    global mouse_x, mouse_y, last_frame, dt
    fade = pygame.Surface((width, height))
    fade.fill(BLACK)
    fading = True
    alpha = 255
    while fading:
        detect_button(song_selection[song_current_select])
        if alpha > 0:
            dt = pygame.time.get_ticks() - last_frame
            dt = delta_to_modifier(dt)
            last_frame = pygame.time.get_ticks()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_close()
            screen.fill(BLACK)
            screen.blit(bg.image, [bg.rect.center[0] - width / 2, bg.rect.center[1] - height / 2])
            sprite.draw(screen)
            bg.alt_update()
            draw_cursor()
            sprite.update()
            draw_text(screen, f'FPS: {int(fps)}/{str(FPS)}', 10, 0, 'big')
            ######################
            fade.set_alpha(alpha)
            screen.blit(fade, (0, 0))
            ######################
            pygame.display.update()
            alpha -= 10 * dt
        else:
            fading = False


def detect_button(surf, invert=None):

    if not invert:

        surf_rect_pos = surf.rect.center
        surf_rect = surf.rect
        surf_pos_x = surf_rect_pos[0]
        surf_pos_y = surf_rect_pos[1]
        surf_width, surf_height = surf_rect[2], surf_rect[3]

        if mouse_x >= (surf_pos_x - (surf_width / 2)) and \
           mouse_x <= (surf_pos_x + (surf_width / 2)) and \
           mouse_y >= (surf_pos_y - (surf_height / 2)) and \
           mouse_y <= (surf_pos_y + (surf_height / 2)):

            if surf.image.get_alpha() < 240:
                alpha_smooth_transform_add(surf, surf.image.get_alpha(), 255)

            return True

        else:

            if surf.image.get_alpha() > 90:
                alpha_smooth_transform_subtract(surf, surf.image.get_alpha(), 90)

    if invert:

        surf_rect_pos = surf.rect.center
        surf_rect = surf.rect
        surf_pos_x = surf_rect_pos[0]
        surf_pos_y = surf_rect_pos[1]
        surf_width, surf_height = surf_rect[2], surf_rect[3]

        if mouse_x >= (surf_pos_x - (surf_width / 2)) and \
           mouse_x <= (surf_pos_x + (surf_width / 2)) and \
           mouse_y >= (surf_pos_y - (surf_height / 2)) and \
           mouse_y <= (surf_pos_y + (surf_height / 2)):

            if surf.image.get_alpha() > 150:
                surf.image.set_alpha(surf.image.get_alpha() - 10 * dt)
            return True

        else:

            if surf.image.get_alpha() < 240:
                surf.image.set_alpha(surf.image.get_alpha() + 10 * dt)


def detect_button_raw(surf):

    surf_rect_pos = surf.rect.center
    surf_rect = surf.rect
    surf_pos_x = surf_rect_pos[0]
    surf_pos_y = surf_rect_pos[1]
    surf_width, surf_height = surf_rect[2], surf_rect[3]

    if mouse_x >= (surf_pos_x - (surf_width / 2)) and \
       mouse_x <= (surf_pos_x + (surf_width / 2)) and \
       mouse_y >= (surf_pos_y - (surf_height / 2)) and \
       mouse_y <= (surf_pos_y + (surf_height / 2)):

        return True


def int_smooth_tranform(now, target):

    if now - 0.05 <= target <= now + 0.05:
        return target

    if target > now:
        return target - 0.2 * dt
    else:
        return target + 0.2 * dt


def alpha_refresh(surface):
    surface.image.set_alpha(0)


def pos_y_jump_to(surface, target):
    surface.pos_y = target


def pos_x_jump_to(surface, target):
    surface.pos_x = target


def pos_jump_to(surface, target=()):
    surface.pos_x = target[0]
    surface.pos_y = target[1]


def smooth_transform_pos_y(surface, target):

    modifier = abs(target - surface.pos_y) * 0.001 * 0.5

    if round(surface.pos_y) < target:
        surface.pos_y += speed * modifier * dt
    if round(surface.pos_y) > target:
        surface.pos_y -= speed * modifier * dt


def alpha_smooth_transform_add(surface, now_alpha, target_alpha):

    if round(now_alpha) < target_alpha:

        modifier = abs((target_alpha - now_alpha)) / 255
        now_alpha += 5 * modifier * dt
        surface.image.set_alpha(now_alpha)


def alpha_smooth_transform_subtract(surface, now_alpha, target_alpha):

    if round(target_alpha) < now_alpha:

        modifier = abs((now_alpha - target_alpha)) / 255
        now_alpha -= 5 * modifier * dt
        surface.image.set_alpha(now_alpha)


def song_selection_updater():

    first_song_pos = song_selection[0].pos_x

    for songs in range(len(song_list) - 1):
        song_selection[songs + 1].pos_x = first_song_pos + (width * (songs + 1))

    target_selection = width_middle - (width * song_current_select)
    modifier = abs(target_selection - song_selection[0].pos_x) * 0.001 * 0.85

    if round(first_song_pos) < target_selection:
        song_selection[0].pos_x += speed * modifier * dt
    if round(first_song_pos) > target_selection:
        song_selection[0].pos_x -= speed * modifier * dt


def song_selection_pos_snap():
    target_selection = width_middle - (width * song_current_select)
    song_selection[0].pos_x = target_selection


def song_selection_audio_system():
    play_music(song_list[song_current_select][audio], time=song_list[song_current_select][play_time])


def play_music(path, time=0):

    pygame.mixer.music.unload()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1, time, fade_ms=1500)


def play_music_long_fade(path):

    pygame.mixer.music.unload()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1, fade_ms=10000)


def scene_handler():

    if run:
        song_selection_pos_snap()
        pos_y_jump_to(logo, height)
        pos_x_jump_to(enter_button, -width)
        pos_x_jump_to(setting_button, width * 1.5)
        sprite.empty()
        sprite.add(main_menu)

        pygame.mixer.music.stop()

        if menu_music_play == 'True':
            play_music_long_fade(menu_music)

        else:
            pass

        for songs in song_selection:
            alpha_refresh(songs)
            pos_y_jump_to(songs, height / 3)

    if run_song_selection:

        sprite.empty()
        sprite.add(back_button, song_selection)
        song_selection_audio_system()


def run_settings():

    global run
    run = False
    pygame.quit()

    os.system('yuGen_data\\skin\\settings.ini')
    os.system('start yuGen.exe')
    sys.exit()


def delta_to_modifier(delta):
    return delta / 1000 * 60


sprite = pygame.sprite.Group()

bg = Background()
setting_button = Setting_button()
enter_button = Enter_button()
back_button = Back_button()
logo = Logo()

song_selection = []

# Generating song selection

for i in range(len(song_list)):
    song_selection.append(Songs(song_list[i][cover], i))


main_menu = logo, setting_button, enter_button

run = True
intro = True
run_song_selection = False
running_gameplay = False
gameplay = False
last_frame = pygame.time.get_ticks()
dt = 0

tan_pos = [width * 0.4, -height]
wy_pos = [width * 0.5, 0]
hang_pos = [width * 0.6, height]
intro_target = height / 2
intro_target_2 = - height
intro_script_pos = -height
intro_checkpoint = 0
end = False
intro_sound.play()
opening = True
while opening:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            dt = 1
            intro_sound.play()
            scene_handler()
            opening = False
    dt = pygame.time.get_ticks() - last_frame
    dt = delta_to_modifier(dt)
    last_frame = pygame.time.get_ticks()
    screen.fill(BLACK)
    draw_text(screen, '[Press any key to skip]', 0, 0, size='big')
    draw_text_centered(screen, 'TAN', tan_pos[0], tan_pos[1], size='large')
    draw_text_centered(screen, 'WY', wy_pos[0], wy_pos[1], size='large')
    draw_text_centered(screen, 'HANG', hang_pos[0], hang_pos[1], size='large')
    draw_text_centered(screen, 'INPIRED BY OSU - 2022', width / 2, intro_script_pos, size='large')
    tan_pos[1] += (intro_target - tan_pos[1]) * 0.1 * dt
    wy_pos[1] += (intro_target - wy_pos[1]) * 0.1 * dt
    hang_pos[1] += (intro_target - hang_pos[1]) * 0.1 * dt
    intro_script_pos += (intro_target_2 - intro_script_pos) * 0.1 * dt
    if tan_pos[1] > intro_target - height * 0.01 and intro_checkpoint == 0:
        intro_target = height * 1.1
        intro_target_2 = height / 2
        intro_checkpoint = 1
        select_sound.play()
    if intro_script_pos > height / 2 - height * 0.01:
        intro_target = - height * 0.2
        intro_target_2 = - height * 0.5
        end = True
        start_sound.play()
    if tan_pos[1] <= intro_target + height * 0.1 and end:
        dt = 1
        intro_sound.play()
        scene_handler()
        break
    pygame.display.update()

while run:

    dt = pygame.time.get_ticks() - last_frame
    dt = delta_to_modifier(dt)
    last_frame = pygame.time.get_ticks()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if logo.image.get_alpha() <= 255:
        logo.image.set_alpha(logo.image.get_alpha() + (speed / 15) * dt)

    if intro:

        if logo.image.get_alpha() >= 255 and bg.image.get_alpha() != 255:

            bg_modifier = (main_menu_background_brightness - bg_alpha) / 255
            bg_alpha += speed / 40 * bg_modifier * dt
            bg.image.set_alpha(bg_alpha)

        else:
            bg.image.set_alpha(0)

    # detection

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            run_menu = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN and logo.image.get_alpha() == 255:

                enter_sound.play()
                run_song_selection = True
                intro = False
                enter_button.image.set_alpha(255)
                setting_button.image.set_alpha(255)
                fade_in()
                scene_handler()
                fade_out()

        if event.type == pygame.MOUSEBUTTONDOWN and \
           event.button == 1 and enter_button.ready_to_press:

            run_song_selection = True
            intro = False
            enter_button.image.set_alpha(255)
            setting_button.image.set_alpha(255)
            enter_sound.play()
            sprite.remove(setting_button)
            fade_in()
            scene_handler()
            fade_out()

        if setting_button.ready_to_press and \
           event.type == pygame.MOUSEBUTTONDOWN and \
           event.button == 1:

            run_settings()

    while run_song_selection:

        dt = pygame.time.get_ticks() - last_frame
        dt = delta_to_modifier(dt)
        last_frame = pygame.time.get_ticks()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        song_press_detected = detect_button(song_selection[song_current_select], True)

        for event in pygame.event.get():

            if song_press_detected and \
                (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                running_gameplay = True
                pygame.mixer.music.stop()
                start_sound.play()
                fade_in()
                song_selection_pos_snap()
                song_selection_updater()
                song_selection[0].pos_x = width_middle - (width * song_current_select)
                current_song_beatmap = song_list[song_current_select][beatmap]
                background = pygame.transform.smoothscale(song_list[song_current_select][cover],
                                                          (width, height)).convert()
                background.set_alpha(30)

                game = Game()
                guide = Guide()
                score = 0
                bps_value = 0
                last_delta_note = 0
                notes = []
                circle_objects = []
                circle_objects_for_scanner = []
                time = 0
                pos = 1
                hit_window = 200
                hit_appear = 800
                hit = 0
                combo_list = []
                hit_effects = []
                start_game_time = 3000
                played = False
                result_screen = False
                for i in current_song_beatmap:
                    notes.append([int(i["time"]) + start_game_time,
                                  [int(i["x"]) * scale_width,
                                  int(i["y"]) * scale_height]])

                max_combo = len(notes)
                scanner = Scanner()
                last_note_time = notes[-1][time]
                end_time = last_note_time + start_game_time

                total_score = 1_000_000
                single_note_score = total_score / len(notes)

                start_time = notes[0][time]
                current_note_time = notes[0][time]
                current_note_pos = notes[0][pos]

                song_to_play = song_list[song_current_select][audio]
                pygame.mixer.music.load(song_to_play)
                circle_image = hit_circle_pic
                circle_rect = circle_image.get_rect()
                circle_size = circle_rect[3]
                delta_note = 0
                last_delta_note_raw = 0
                last_delta_note_future = 0

                fade = pygame.Surface((width, height))
                fade.fill(BLACK)
                fade.set_alpha(0)
                alpha = 255
                while True:
                    if alpha > 0:
                        dt = pygame.time.get_ticks() - last_frame
                        dt = delta_to_modifier(dt)
                        last_frame = pygame.time.get_ticks()
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        check_close()
                        screen.fill(BLACK)
                        screen.blit(background, [0,
                                                 0])
                        game.accuracy = ((game.hits + 1) / (game.passed + 1)) * 100
                        game.accuracy = '{:.2f}'.format(game.accuracy)
                        guide.update()
                        draw_text_rgb(screen, 'score ' + str(int(score)),
                                              (255, 223, 255 - 255 * score / 1_000_000), 0, 0, 'large')
                        draw_text(screen, f'{str(game.combo)} x combo', 0, height * 0.05, 'big')
                        draw_text(screen, f'FPS: {str(int(clock.get_fps()))}', 0, height * 0.93, 'big')
                        bps_value = abs(last_delta_note)
                        bps = f"BPS: {str('{:.1f}'.format(abs(last_delta_note)))}"
                        draw_text(screen, bps, width * 0.88, height * 0.18, 'large')
                        draw_text(screen, str(game.accuracy) + '%', width * 0.9, height * 0.24, 'big')

                        ######################
                        fade.set_alpha(alpha)
                        screen.blit(fade, (0, 0))
                        ######################
                        pygame.display.update()
                        alpha -= 10 * dt
                    else:
                        break

                now_time = pygame.time.get_ticks()
                elapsed_time = pygame.time.get_ticks() - now_time

            if event.type == pygame.QUIT:
                run = False
                run_song_selection = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    back_sound.play()
                    run_song_selection = False
                    fade_in()
                    scene_handler()
                    fade_out()

                if event.key == pygame.K_a and song_current_select > 0:
                    song_current_select -= 1
                    select_sound.play()
                    song_selection_audio_system()

                if event.key == pygame.K_d and song_current_select < len(song_list) - 1:
                    song_current_select += 1
                    select_sound.play()
                    song_selection_audio_system()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 4 and song_current_select > 0:
                    song_current_select -= 1
                    select_sound.play()
                    song_selection_audio_system()

                if event.button == 5 and song_current_select < len(song_list) - 1:
                    song_current_select += 1
                    select_sound.play()
                    song_selection_audio_system()

                if back_button.ready_to_press and \
                   event.button == 1:
                    run_song_selection = False
                    back_sound.play()
                    fade_in()
                    song_selection_pos_snap()
                    sprite.update()
                    scene_handler()
                    fade_out()

        while running_gameplay:

            dt = pygame.time.get_ticks() - last_frame
            dt = delta_to_modifier(dt)
            last_frame = pygame.time.get_ticks()

            screen.fill(BLACK)
            screen.blit(background, [0, 0])

            elapsed_time = pygame.time.get_ticks() - now_time

            if elapsed_time > start_game_time and not played:
                pygame.mixer.music.play()
                played = True

            for event in pygame.event.get():

                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running_gameplay = False
                    scene_handler()
                    fade_out()

                if running_gameplay and \
                   len(circle_objects) != 0 and event.type == pygame.KEYDOWN:
                    if circle_objects[0].can_press:
                        hit_sound.play()
                        hit_effects.append(Hit(circle_objects[0].pos))
                        circle_objects.pop(0)
                        hit += 0.9 + ((((game.combo + 1) / (max_combo + 1)) * 2) * 0.1)
                        game.combo += 1
                        game.hits += 1
                        game.passed += 1
                        combo_list.append(game.combo)
                    else:
                        game.combo = 0
                        game.bad += 1
                        game.passed += 1
                        intro_sound.play()

            if running_gameplay:

                if elapsed_time >= (current_note_time - hit_window - hit_appear) and len(notes) > 0:
                    circle_objects.append(Circle(current_note_pos, current_note_time))
                    circle_objects_for_scanner.append([current_note_pos, current_note_time])
                    notes.pop(0)
                overlaps = 1
                text_overlap = []
                for i in circle_objects:
                    i.update()
                if len(circle_objects_for_scanner) > 1:
                    delta_note = 1000 / (circle_objects_for_scanner[1][1] - circle_objects_for_scanner[0][1])
                    for i in range(len(circle_objects_for_scanner) - 1):
                        if circle_objects_for_scanner[i][0] == circle_objects_for_scanner[i + 1][0]:
                            overlaps += 1
                        else:
                            if overlaps > 1:
                                text_overlap.append([overlaps, circle_objects_for_scanner[i][0]])
                                break
                else:
                    delta_note = 0

                if len(text_overlap) > 0:
                    for i in text_overlap:
                        draw_text_centered_alpha(screen, str(i[0]), i[1][0], i[1][1],
                                                 'big', alpha=100)
                for i in hit_effects:
                    i.update()
                if len(notes) > 0:
                    current_note_time = notes[0][time]
                    current_note_pos = notes[0][pos]
                score = hit * single_note_score
                if len(circle_objects_for_scanner) > 0:
                    scanner.update()
                game.accuracy = ((game.hits + 1) / (game.passed + 1)) * 100
                game.accuracy = '{:.2f}'.format(game.accuracy)
                guide.update()
                draw_text_rgb(screen, 'score ' + str(int(score)),
                                      (255, 223, 255 - 255 * score / 1_000_000), 0, 0, 'large')
                draw_text(screen, f'{str(game.combo)} x combo', 0, height * 0.05, 'big')
                draw_text(screen, f'FPS: {str(int(clock.get_fps()))}', 0, height * 0.93, 'big')
                bps_value = abs(last_delta_note)
                bps = f"BPS: {str('{:.1f}'.format(abs(last_delta_note)))}"
                draw_text(screen, bps, width * 0.88, height * 0.18, 'large')
                draw_text(screen, str(game.accuracy) + '%', width * 0.9, height * 0.24, 'big')
                pygame.draw.line(screen, WHITE, [0, height], [width * (elapsed_time / last_note_time), height],
                                 int(line_width))
                last_delta_note = int_smooth_tranform(delta_note, last_delta_note)
                pygame.display.update()
                clock.tick(-1)

                if elapsed_time > end_time:

                    result_screen = True
                    running_gameplay = False
                    fade = pygame.Surface((width, height))
                    fade.fill(BLACK)
                    alpha = 0
                    while True:
                        if alpha < 255:
                            dt = pygame.time.get_ticks() - last_frame
                            dt = delta_to_modifier(dt)
                            last_frame = pygame.time.get_ticks()
                            check_close()
                            screen.fill(BLACK)
                            screen.blit(background, [0,
                                                     0])
                            game.accuracy = ((game.hits + 1) / (game.passed + 1)) * 100
                            game.accuracy = '{:.2f}'.format(game.accuracy)
                            guide.update()
                            draw_text_rgb(screen, 'score ' + str(int(score)),
                                                  (255, 223, 255 - 255 * score / 1_000_000), 0, 0, 'large')
                            draw_text(screen, f'{str(game.combo)} x combo', 0, height * 0.05, 'big')
                            draw_text(screen, f'FPS: {str(int(clock.get_fps()))}', 0, height * 0.93, 'big')
                            bps_value = abs(last_delta_note)
                            bps = f"BPS: {str('{:.1f}'.format(abs(last_delta_note)))}"
                            draw_text(screen, bps, width * 0.88, height * 0.18, 'large')
                            draw_text(screen, str(game.accuracy) + '%', width * 0.9, height * 0.24, 'big')

                            pygame.draw.line(screen, WHITE, [0, height],
                                             [width * (elapsed_time / last_note_time), height],
                                             int(line_width))
                            ######################
                            fade.set_alpha(alpha)
                            screen.blit(fade, (0, 0))
                            ######################
                            pygame.display.update()
                            alpha += 10 * dt
                        else:
                            break
                    alpha = 255
                    score = int(score)

                    if score > int(song_list[song_current_select][high_score]):
                        with open(song_list[song_current_select][beatmap_path], "r") as jsonFile:
                            data = json.load(jsonFile)
                        data["score"] = int(score)
                        with open(song_list[song_current_select][beatmap_path], "w") as jsonFile:
                            json.dump(data, jsonFile)

                        song_list[song_current_select][high_score] = int(score)

                    rank_image = game.judge_rank(score)
                    while True:
                        dt = pygame.time.get_ticks() - last_frame
                        dt = delta_to_modifier(dt)
                        last_frame = pygame.time.get_ticks()
                        if alpha > 0:
                            check_close()
                            screen.fill(BLACK)
                            screen.blit(background, (0, 0))
                            screen.blit(rank_image, [width * 0.6, height / 2 - rank_image_radius])
                            draw_text(screen, f'Score {str(int(score))}', 0, 80, 'large')
                            draw_text(screen, f'{songs_files[song_current_select]}', 0, 0, 'large')
                            if len(combo_list) > 0:
                                draw_text(screen, f'Highest Combo: {str(max(combo_list))} / {str(max_combo)}',
                                          0, 140, 'big')
                            else:
                                draw_text(screen, f'Highest Combo: 0 / {str(max_combo)}', 0, height * 0.16, 'big')
                            draw_text(screen, f'hits {str(int(game.hits))}', 0, height * 0.4, 'big')
                            draw_text(screen, f'Miss {str(int(game.misses))}', 0, height * 0.48, 'big')
                            draw_text(screen, f'Bad {str(int(game.bad))}', 0, height * 0.56, 'big')
                            draw_text(screen, f'Accuracy {str(game.accuracy)}%', 0, height * 0.64, 'big')
                            draw_text_centered(screen, 'Back to menu [Enter]', width / 2, height * 0.95, 'big')
                            ######################
                            alpha -= 10 * dt
                            fade.set_alpha(alpha)
                            screen.blit(fade, (0, 0))
                            ######################
                            pygame.display.update()
                        else:
                            break

            while result_screen:
                dt = pygame.time.get_ticks() - last_frame
                dt = delta_to_modifier(dt)
                last_frame = pygame.time.get_ticks()
                screen.fill(BLACK)
                screen.blit(background, (0, 0))
                screen.blit(rank_image, [width * 0.6, height / 2 - rank_image_radius])
                draw_text(screen, f'Score {str(int(score))}', 0, 80, 'large')
                draw_text(screen, f'{songs_files[song_current_select]}', 0, 0, 'large')
                if len(combo_list) > 0:
                    draw_text(screen, f'Highest Combo: {str(max(combo_list))} / {str(max_combo)}', 0, 140, 'big')
                else:
                    draw_text(screen, f'Highest Combo: 0 / {str(max_combo)}', 0, height * 0.16, 'big')
                draw_text(screen, f'hits {str(int(game.hits))}', 0, height * 0.4, 'big')
                draw_text(screen, f'Miss {str(int(game.misses))}', 0, height * 0.48, 'big')
                draw_text(screen, f'Bad {str(int(game.bad))}', 0, height * 0.56, 'big')
                draw_text(screen, f'Accuracy {str(game.accuracy)}%', 0, height * 0.64, 'big')
                draw_text_centered(screen, 'Back to menu [Enter]', width / 2, height * 0.95, 'big')

                for event in pygame.event.get():
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.QUIT:
                        enter_sound.play()
                        alpha = 0
                        while True:
                            dt = pygame.time.get_ticks() - last_frame
                            dt = delta_to_modifier(dt)
                            last_frame = pygame.time.get_ticks()
                            if alpha < 255:
                                check_close()
                                screen.fill(BLACK)
                                screen.blit(background, (0, 0))
                                screen.blit(rank_image, [width * 0.6, height / 2 - rank_image_radius])
                                draw_text(screen, f'Score {str(int(score))}', 0, 80, 'large')
                                draw_text(screen, f'{songs_files[song_current_select]}', 0, 0, 'large')
                                if len(combo_list) > 0:
                                    draw_text(screen, f'Highest Combo: {str(max(combo_list))} / {str(max_combo)}',
                                              0, 140, 'big')
                                else:
                                    draw_text(screen, f'Highest Combo: 0 / {str(max_combo)}',
                                              0, height * 0.16, 'big')
                                draw_text(screen, f'hits {str(int(game.hits))}', 0, height * 0.4, 'big')
                                draw_text(screen, f'Miss {str(int(game.misses))}', 0, height * 0.48, 'big')
                                draw_text(screen, f'Bad {str(int(game.bad))}', 0, height * 0.56, 'big')
                                draw_text(screen, f'Accuracy {str(game.accuracy)}%', 0, height * 0.64, 'big')
                                draw_text_centered(screen, 'Back to menu [Enter]', width / 2, height * 0.95, 'big')
                                ######################
                                alpha += 10 * dt
                                fade.set_alpha(alpha)
                                screen.blit(fade, (0, 0))
                                ######################
                                pygame.display.update()
                            else:
                                break
                        result_screen = False
                        scene_handler()
                        fade_out()
                clock.tick(-1)
                pygame.display.update()

        screen.fill(BLACK)
        screen.blit(bg.image, [bg.rect.center[0] - width / 2, bg.rect.center[1] - height / 2])
        bg.alt_update()
        sprite.draw(screen)
        sprite.update()
        # border = pygame.rect.Rect(0, 0, width, height)
        # pygame.draw.rect(screen, WHITE, border, 1)
        fps = clock.get_fps()
        draw_text(screen, f'FPS: {int(fps)}/{str(FPS)}', 10, 0, 'big')
        draw_cursor()
        song_selection_updater()
        pygame.display.update()
        clock.tick(FPS)

    # home_screen
    screen.fill(BLACK)
    screen.blit(bg.image, [bg.rect.center[0] - width / 2, bg.rect.center[1] - height / 2])
    sprite.update()
    sprite.draw(screen)
    bg.alt_update()
    # border = pygame.rect.Rect(0, 0, width, height)
    # pygame.draw.rect(screen, WHITE, border, 1)
    fps = clock.get_fps()
    draw_text(screen, f'FPS: {int(fps)}/{str(FPS)}', 10, 0, 'big')
    draw_cursor()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
