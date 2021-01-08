import pygame,sys,os,random

# Pygame Window
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird')
font = pygame.font.Font('Western.ttf',60)

# Variables
FPS = 120
SCREENWIDTH = 576
SCREENHEIGHT = 700
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
sounds = []
images = []
playerx = int(88)
playery = int(150)
gravity = 0.25
bird_movement = 0
End = False
list_pip = []
collision = False
ran = 0
score = 0

# Getting all the sound and pics##################################################
for i in range(5):
    image = pygame.image.load('flappy'+str(i)+'.png').convert_alpha()
    images.append(image)
status = [0,1,2,3,4,5]
image = pygame.transform.rotate(pygame.image.load('flappy3.png').convert_alpha(),180)
images.append(image)


images[status[1]] = pygame.transform.scale2x(images[status[1]])


images[status[2]] = pygame.transform.scale2x(images[status[2]]) # Zoom Bird
rect_of_bird = images[status[2]].get_rect(center=(playerx,playery))


for i in range(5):
    sound = pygame.mixer.Sound('sound'+str(i)+'.wav')
    sounds.append(sound)
    sound_status = [0,1,2,3,4]
 #####################################################################################   
# All Functions
def draw_base():
    SCREEN.blit(images[status[1]],(floor_x,600))
    SCREEN.blit(images[status[1]],(floor_x + 576,600)) 
floor_x = 0       
   
def show_flying_message():
    SCREEN.blit(images[status[6]],(188,250))
    
def desplay_over(x,y,text):
        score_surface = font.render(text,True,(255,255,255))        
        score_rect = score_surface.get_rect(center = (x,y))
        SCREEN.blit(score_surface,score_rect)

def create_pipe():
    global ran
    radom_pipe = random.choice([400,430,450,500,520])
    ran = radom_pipe
    new_pipe = images[status[3]].get_rect(midtop = (700,radom_pipe))
    top_pipe = images[status[3]].get_rect(midbottom = (700,radom_pipe -200))
    return new_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 650:
            SCREEN.blit(images[status[3]],pipe)
        else:
            SCREEN.blit(images[status[5]],pipe)      
 
def display_over():
        sounds[sound_status[0]].play()
        desplay_over(288,200,'GAME Over')
        desplay_over(288,300,'Press Space To')
        desplay_over(288,400,'Play Again')   
        
def score_display():
    dis = 'Score:{}'.format(score)
    score_surface = font.render(dis,True,(255,255,255))     
    score_rect = score_surface.get_rect(center = (288,50))
    SCREEN.blit(score_surface,score_rect)    
             
     
Random = pygame.USEREVENT +1 
pygame.time.set_timer(Random,1200)
                          


if __name__ == "__main__":
    while True:
        #print(ran)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and End == True:
                    rect_of_bird.center = (88,150)
                    list_pip.clear()
                    bird_movement = 0
                    score = 0
                    End = False
                    
                    
                
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 or event.button == 3:
                    bird_movement = 0
                    bird_movement -= 8
                    sounds[sound_status[4]].play()
            if event.type == Random:
                list_pip.extend(create_pipe())     
                    
        
        if not End:
            
            SCREEN.blit(pygame.transform.scale(images[status[0]],(576,700)), (0,0)) #Bg
            bird_movement += gravity
            rect_of_bird.centery += bird_movement
            if ran:        
                if rect_of_bird.centery > ran and rect_of_bird.centery < ran+100:
                    print('hello')
                    score += 1
                    sounds[sound_status[2]].play()
                    ran = 0
                    
                        
            for pipe in list_pip:
                if rect_of_bird.colliderect(pipe):
                    print('collision')
                    End = True
                    display_over()
     
            move_pipes(list_pip)
            draw_pipes(list_pip)
            score_display()
        SCREEN.blit(images[status[2]],rect_of_bird)
        
        
        

        
        floor_x -= 1
        draw_base()
        if floor_x <= -576:
            floor_x = 0
 
        if rect_of_bird.centery > 600 or rect_of_bird.centery < 0 :
            if rect_of_bird.centery < 0:
                rect_of_bird.centery = 0                         

            else:       
                rect_of_bird.centery = 580
            End = True
            display_over()
            
        pygame.display.update()
        clock.tick(120)