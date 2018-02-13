import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
#800x600
pixAr[40][200] = red

pygame.draw.line(gameDisplay,green,(100,200),(100,500),4)
# rect(where,color,(startxtopleft,startytopleft,width,height))
pygame.draw.rect(gameDisplay,blue,(400,400,50,20))
pygame.draw.circle(gameDisplay,white,(150,150),75)
pygame.draw.polygon(gameDisplay,red,((25,75),(76,125),(250,375),(500,300),(60,520)))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	pygame.display.update()