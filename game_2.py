import pygame,random
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
GREEN = (0,255,0)


clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    "The class is the player-controlled sprite. "
 
    # -- Methods
    def __init__(self, x, y, length, width):
        "Constructor function"
        # Call the parent's constructor
        super().__init__()

        self.length = length
        self.width = width
        # Set height, width
        self.image = pygame.Surface([self.length, self.width])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        " Change the speed of the player"
        self.change_x += x
        self.change_y += y
 
    def update(self):
        " Find a new position for the player"
        new_x = self.rect.x + self.change_x
        new_y = self.rect.y + self.change_y
        if new_x <= screen_width - self.length and new_x >= 0:
            self.rect.x = new_x
        if new_y <= screen_height - 100 and new_y > 0:
            self.rect.y = new_y

class Block(Player):
    def update(self):
        " Find a new position for the player"
        new_x = self.rect.x + self.change_x
        new_y = self.rect.y + self.change_y
        if new_x <= screen_width - self.length and new_x > 0:
            self.rect.x = new_x
        else:
            self.kill()
        if new_y <= 400 and new_y > 150:
            self.rect.y = new_y
        else:
            self.kill()

class Projectile(Player):
    def update(self):
        " Find a new position for the player"
        new_x = self.rect.x + self.change_x
        new_y = self.rect.y + self.change_y
        if new_x <= screen_width - self.length and new_x > 0:
            self.rect.x = new_x
        else:
            self.kill()
        if new_y <= screen_height - self.width and new_y > 0:
            self.rect.y = new_y
        else:
            self.kill()
 
class Game():                                                                        

    def main(self, screen):
        clock = pygame.time.Clock()

        enemy_life = 5
        player_life = 5 
        count = 0
        lst = [0]
        done = True
        shoot = False
        enemy_count = 0
        player_count = 0
        speed = 2
        vel = 5
        enemys = 50
        dots = 500
        score = 0 

        sprites = pygame.sprite.Group()
        obstacle_lst = pygame.sprite.Group()
        dots_lst = pygame.sprite.GroupSingle()
        ball = pygame.sprite.Group()
        user_lst = pygame.sprite.Group()
        user = pygame.sprite.GroupSingle()

        player = Player(screen_width / 2, screen_height - 18, 40,18) 
        enemy = Player(screen_width - 80, 90, 80,5)
        enemy.image.fill(BLUE)
        wall = Player(100,450, 80,5)
        wall2 = Player(400,500, 100,5)
        wall3 = Player(700,450, 80,5)
        wall.image.fill(BLUE)
        wall2.image.fill(BLUE)
        wall3.image.fill(BLUE)

        user.add(player)
        ball.add(wall)
        ball.add(wall2)
        ball.add(wall3)
        ball.add(enemy)
        


        font = pygame.font.SysFont('comicsans', 30, True,True)



        while done:
            clock.tick(60)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.changespeed(-vel, 0)
                    elif event.key == pygame.K_RIGHT:
                        player.changespeed(vel, 0)
 
        # Reset speed when key goes up
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.changespeed(vel, 0)
                    elif event.key == pygame.K_RIGHT:
                        player.changespeed(-vel, 0)

            keys = pygame.key.get_pressed()
                
            
            if keys[pygame.K_SPACE]:
                shoot = True
                players = Projectile(player.rect.centerx - 5,player.rect.centery , 2,10)
                players1 = Projectile(player.rect.centerx + 5,player.rect.centery , 2,10)
                if player_count == 2:
                    user_lst.add(players)
                    user_lst.add(players1)
                    player_count = 0
                     
                else:
                    player_count += 1
                players.changespeed(0, -10)
                players1.changespeed(0,-10)

            if len(sprites) < 1:
                pygame.time.delay(100)
                enemy1 = Player(screen_width / 2, 40, 50,10)
                enemy2 = Player(screen_width / 2, 40, 50,10)
                enemy1.image.fill(GREEN)
                enemy2.image.fill(GREEN)
                sprites.add(enemy1)
                sprites.add(enemy2)
                
            
            obstacle = Block(random.randint(0,885),random.randint(150,400),15,15)
            obstacle.image.fill(RED)
            obstacle_lst.add(obstacle)

            dot = Player(random.randint(20,880),random.randint(150,400),20,20)
            dot.image.fill(YELLOW)
            
            dots_lst.update()
            user.update()
            ball.update()
            obstacle_lst.update()
            
            if count == 200:
                dots_lst.add(dot)                
                count = 0
            else:
                count += 1


            if enemy_count == 5:
                enemyshot  = Projectile(enemy1.rect.centerx - 5 ,enemy1.rect.centery, 2,10)
                enemyshot1  = Projectile(enemy1.rect.centerx + 5 ,enemy1.rect.centery, 2,10)
                enemyshot2  = Projectile(enemy2.rect.centerx - 5 ,enemy1.rect.centery, 2,10)
                enemyshot3  = Projectile(enemy2.rect.centerx + 5 ,enemy1.rect.centery, 2,10)
                enemyshot.image.fill(YELLOW)
                enemyshot1.image.fill(YELLOW)
                enemyshot2.image.fill(YELLOW)
                enemyshot3.image.fill(YELLOW)

                if enemy1 in sprites and enemy2 in sprites:
                    obstacle_lst.add(enemyshot)
                    obstacle_lst.add(enemyshot1)
                    enemyshot.changespeed(0, 8)
                    enemyshot1.changespeed(0,8)

                    obstacle_lst.add(enemyshot2)
                    obstacle_lst.add(enemyshot3)
                    enemyshot2.changespeed(0, 8)
                    enemyshot3.changespeed(0,8)
                  
                elif enemy1 in sprites:
                    obstacle_lst.add(enemyshot)
                    obstacle_lst.add(enemyshot1)
                    enemyshot.changespeed(0, 8)
                    enemyshot1.changespeed(0,8)

                elif enemy2 in sprites:
                    obstacle_lst.add(enemyshot2)
                    obstacle_lst.add(enemyshot3)
                    enemyshot2.changespeed(0, 8)
                    enemyshot3.changespeed(0,8)

                enemy_count = 0

            else:
                enemy_count += 1

           
            # -- Draw everything
            # Clear screen
            screen.fill(BLACK)
            
            ran = random.randint(1,4)
            lst.append(ran)

            while lst[-1] == lst[-2]:
                ran = random.randint(1,4)
                lst.append(ran)
                
            if enemy.rect.left <= 0:
                enemy.changespeed(speed + 8,0)
            elif enemy.rect.right >= screen_width:
                enemy.changespeed(-(speed + 8) ,0)

            if enemy1.rect.left <= 200:
                enemy1.changespeed(speed,0)
            elif enemy1.rect.right >= screen_width:
                enemy1.changespeed(-speed ,0)

            if enemy2.rect.left <= 200:
                enemy2.changespeed(speed,0)
            elif enemy2.rect.right >= screen_width:
                enemy2.changespeed(-speed ,0)
                     
            if ran == 1:
                obstacle.changespeed(speed,0)
                enemy2.changespeed(-speed,0)
            elif ran == 2:
                obstacle.changespeed(-speed,0)
                enemy1.changespeed(-speed,0)
            elif ran == 3:
                obstacle.changespeed(0,speed)
            else:
                obstacle.changespeed(0,-speed)
            # Draw sprites
                
                


            players_hit = pygame.sprite.groupcollide(obstacle_lst, user_lst, True,True)
           # players1_hit = pygame.sprite.spritecollide(obstacle_lst, user,True,True)       

            wall_hit = pygame.sprite.groupcollide(user_lst , ball, True, False)
            dot_hit = pygame.sprite.groupcollide(user_lst,dots_lst,True,True)
            enemy_hit = pygame.sprite.groupcollide(user_lst,sprites,False,True)
            obstacle_hit = pygame.sprite.groupcollide(ball ,obstacle_lst , False, True)
            user_hit = pygame.sprite.groupcollide(user ,obstacle_lst , False, True)
            player_life -= len(user_hit)
            score += (len(dot_hit) * 10)
            score += (len(enemy_hit) * 100)


            user_lst.update()
            user.update()
            sprites.update()
            screen.fill(BLACK)
            sprites.draw(screen)
            user.draw(screen)
            obstacle_lst.draw(screen)
            ball.draw(screen)
            dots_lst.draw(screen)
            user_lst.draw(screen)

            if player_life == 0:
                done = False
            text = font.render('Score: ' + str(score), 1, WHITE)
            users_live = font.render('User: ' + '0'*player_life , 1, WHITE)
            screen.blit(text, (750, 10))
            screen.blit(users_live,(10,10))
               
            pygame.display.flip()

        screen.fill((0,0,0))
        font = pygame.font.SysFont('comicsans', 100, True,True)
        text = font.render('GAME OVER' , 1, WHITE)
        text1 = font.render('Score = ' + str(score),1,WHITE)
        screen.blit(text, (200, 200))
        screen.blit(text1, (250, 300))
        pygame.display.flip()
        pygame.time.delay(500)
        pygame.quit()

      
 
if __name__ == '__main__':
    pygame.init()
    screen_width = 900
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mission Impossible")
    Game().main(screen)
