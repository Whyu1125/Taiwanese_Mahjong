import random
import pygame
import time
pygame.init()
screen_width, screen_height = (1200,650)
screen = pygame.display.set_mode((1200,650), 0, 32)
#font = pygame.font.Font('C:\Windows\Fonts\kaiu.ttf', 36)
font = pygame.font.SysFont("arial", 16)
t1=pygame.image.load('Image/MJt1.gif').convert()
t2=pygame.image.load('Image/MJt2.gif').convert()
t3=pygame.image.load('Image/MJt3.gif').convert()
t4=pygame.image.load('Image/MJt4.gif').convert()
t5=pygame.image.load('Image/MJt5.gif').convert()
t6=pygame.image.load('Image/MJt6.gif').convert()
t7=pygame.image.load('Image/MJt7.gif').convert()
t8=pygame.image.load('Image/MJt8.gif').convert()
t9=pygame.image.load('Image/MJt9.gif').convert()

t2s=pygame.image.load('Image/MJt2s.gif').convert()
t3s=pygame.image.load('Image/MJt3s.gif').convert()
t6s=pygame.image.load('Image/MJt6s.gif').convert()
t7s=pygame.image.load('Image/MJt7s.gif').convert()
t9s=pygame.image.load('Image/MJt9s.gif').convert()

w1=pygame.image.load('Image/MJw1.gif').convert()
w2=pygame.image.load('Image/MJw2.gif').convert()
w3=pygame.image.load('Image/MJw3.gif').convert()
w4=pygame.image.load('Image/MJw4.gif').convert()
w5=pygame.image.load('Image/MJw5.gif').convert()
w6=pygame.image.load('Image/MJw6.gif').convert()
w7=pygame.image.load('Image/MJw7.gif').convert()
w8=pygame.image.load('Image/MJw8.gif').convert()
w9=pygame.image.load('Image/MJw9.gif').convert()

w1s=pygame.image.load('Image/MJw1s.gif').convert()
w2s=pygame.image.load('Image/MJw2s.gif').convert()
w3s=pygame.image.load('Image/MJw3s.gif').convert()
w4s=pygame.image.load('Image/MJw4s.gif').convert()
w5s=pygame.image.load('Image/MJw5s.gif').convert()
w6s=pygame.image.load('Image/MJw6s.gif').convert()
w7s=pygame.image.load('Image/MJw7s.gif').convert()
w8s=pygame.image.load('Image/MJw8s.gif').convert()
w9s=pygame.image.load('Image/MJw9s.gif').convert()

s1=pygame.image.load('Image/MJs1.gif').convert()
s2=pygame.image.load('Image/MJs2.gif').convert()
s3=pygame.image.load('Image/MJs3.gif').convert()
s4=pygame.image.load('Image/MJs4.gif').convert()
s5=pygame.image.load('Image/MJs5.gif').convert()
s6=pygame.image.load('Image/MJs6.gif').convert()
s7=pygame.image.load('Image/MJs7.gif').convert()
s8=pygame.image.load('Image/MJs8.gif').convert()
s9=pygame.image.load('Image/MJs9.gif').convert()

s1s=pygame.image.load('Image/MJs1s.gif').convert()
s2s=pygame.image.load('Image/MJs2s.gif').convert()
s3s=pygame.image.load('Image/MJs3s.gif').convert()
s6s=pygame.image.load('Image/MJs6s.gif').convert()
s7s=pygame.image.load('Image/MJs7s.gif').convert()
s8s=pygame.image.load('Image/MJs8s.gif').convert()
s9s=pygame.image.load('Image/MJs9s.gif').convert()

b1=pygame.image.load('Image/MJf1.gif').convert()
b2=pygame.image.load('Image/MJf2.gif').convert()
b3=pygame.image.load('Image/MJf3.gif').convert()
b4=pygame.image.load('Image/MJf4.gif').convert()

b1s=pygame.image.load('Image/MJf1s.gif').convert()
b2s=pygame.image.load('Image/MJf2s.gif').convert()
b3s=pygame.image.load('Image/MJf3s.gif').convert()
b4s=pygame.image.load('Image/MJf4s.gif').convert()

b5=pygame.image.load('Image/MJd1.gif').convert()
b6=pygame.image.load('Image/MJd2.gif').convert()
b7=pygame.image.load('Image/MJd3.gif').convert()

b5s=pygame.image.load('Image/MJd1s.gif').convert()
b6s=pygame.image.load('Image/MJd2s.gif').convert()

f1r=pygame.image.load('Image/MJh1.gif').convert()
f2r=pygame.image.load('Image/MJh2.gif').convert()
f3r=pygame.image.load('Image/MJh3.gif').convert()
f4r=pygame.image.load('Image/MJh4.gif').convert()
f1b=pygame.image.load('Image/MJh5.gif').convert()
f2b=pygame.image.load('Image/MJh6.gif').convert()
f3b=pygame.image.load('Image/MJh7.gif').convert()
f4b=pygame.image.load('Image/MJh8.gif').convert()

host=pygame.image.load('Image/host.gif').convert()
west=pygame.image.load('Image/l2.gif').convert()
north=pygame.image.load('Image/l3.gif').convert()
east=pygame.image.load('Image/l0.gif').convert()
south=pygame.image.load('Image/l1.gif').convert()

buttonb=pygame.image.load('Image/buttonb.gif').convert()
buttonb=pygame.transform.scale(buttonb,(60,60))

mjb=pygame.image.load('Image/mjb.gif').convert()
mjback=pygame.image.load('Image/mjback.gif').convert()

host=pygame.image.load('Image/host.gif').convert()

background = pygame.image.load('Image/Nostalgy.gif').convert()

def card_to_image(card):
    ide=str(card)
    if ide=='t1':
        return t1
    if ide=='t2':
        return t2
    if ide=='t3':
        return t3
    if ide=='t4':
        return t4
    if ide=='t5':
        return t5
    if ide=='t6':
        return t6
    if ide=='t7':
        return t7
    if ide=='t8':
        return t8
    if ide=='t9':
        return t9
    if ide=='w1':
        return w1
    if ide=='w2':
        return w2
    if ide=='w3':
        return w3
    if ide=='w4':
        return w4
    if ide=='w5':
        return w5
    if ide=='w6':
        return w6
    if ide=='w7':
        return w7
    if ide=='w8':
        return w8
    if ide=='w9':
        return w9
    if ide=='s1':
        return s1
    if ide=='s2':
        return s2
    if ide=='s3':
        return s3
    if ide=='s4':
        return s4
    if ide=='s5':
        return s5
    if ide=='s6':
        return s6
    if ide=='s7':
        return s7
    if ide=='s8':
        return s8
    if ide=='s9':
        return s9
    if ide=='b1':
        return b1
    if ide=='b2':
        return b2
    if ide=='b3':
        return b3
    if ide=='b4':
        return b4
    if ide=='b5':
        return b5
    if ide=='b6':
        return b6
    if ide=='b7':
        return b7
    if ide=='f1r':
        return f1r
    if ide=='f2r':
        return f2r
    if ide=='f3r':
        return f3r
    if ide=='f4r':
        return f4r
    if ide=='f1b':
        return f1b
    if ide=='f2b':
        return f2b
    if ide=='f3b':
        return f3b
    if ide=='f4b':
        return f4b

def card_to_image_show(card):
    ide=str(card)
    image=None
    if ide=='t1':
        image = t1
    if ide=='t2':
        image = t2s
    if ide=='t3':
        image = t3s
    if ide=='t4':
        image = t4
    if ide=='t5':
        image = t5
    if ide=='t6':
        image = t6s
    if ide=='t7':
        image = t7s
    if ide=='t8':
        image = t8
    if ide=='t9':
        image = t9s
    if ide=='w1':
        image = w1s
    if ide=='w2':
        image = w2s
    if ide=='w3':
        image = w3s
    if ide=='w4':
        image = w4s
    if ide=='w5':
        image = w5s
    if ide=='w6':
        image = w6s
    if ide=='w7':
        image = w7s
    if ide=='w8':
        image = w8s
    if ide=='w9':
        image = w9s
    if ide=='s1':
        image = s1s
    if ide=='s2':
        image = s2s
    if ide=='s3':
        image = s3s
    if ide=='s4':
        image = s4
    if ide=='s5':
        image = s5
    if ide=='s6':
        image = s6s
    if ide=='s7':
        image = s7s
    if ide=='s8':
        image = s8s
    if ide=='s9':
        image = s9s
    if ide=='b1':
        image = b1s
    if ide=='b2':
        image = b2s
    if ide=='b3':
        image = b3s
    if ide=='b4':
        image = b4s
    if ide=='b5':
        image = b5s
    if ide=='b6':
        image = b6s
    if ide=='b7':
        image = b7  
    return pygame.transform.rotate(image,180)

def draw_start_player(game):
    direction=num_to_seat(game)
    text='??????%s???'%direction
    text=font.render(text,50,(0,0,0))
    screen.blit(text,(500,400))
def draw_host(game,rot):
    host_loc=[(1030,590),(1080,130),(140,100),(80,480)]
    i=(-rot+game+4)%4
    screen.blit(host,host_loc[i])
def draw_seat(game,rot=0):
    wind=[east,south,west,north]
    wind_loc=[(960,590),(1080,60),(210,100),(80,550)]
    for i in range(4):
        index=(4+i-rot)%4
        screen.blit(wind[i],wind_loc[index])
    draw_host(game,rot)
def draw_background():
    for y in range(0,screen_height,background.get_height()):
        for x in range(0,screen_width,background.get_width()):
            screen.blit(background,(x,y))
def draw_table(table):
    for i in range(len(table.cards)):
        row=i//16
        column=i%16
        pic = card_to_image(table.cards[i])
        screen.blit(pic,(300+(pic.get_width()-10)*column,200+(pic.get_height()-5)*row))
def draw_top(board,wind,deck_down):
    text_wind='%s???%s???'%(num_to_seat(wind),num_to_seat(board))
    text_remaining='??????%d??????'%(len(deck_down.cards)-16)
    text_all=text_wind+' '*10+text_remaining
    text_all=font.render(text_all,50,(0,0,0))
    screen.blit(text_all,(300,10))
def display_all(game,circle,deck,table):
    draw_background()
    draw_table(table)
    draw_top(game,circle,deck)

def draw_card(player,seat=0,status=True):
    mjback_new=pygame.transform.scale(mjback,(44,53))
    mjb_new=pygame.transform.scale(mjb,(44,53))
    mjb_new=pygame.transform.rotate(mjb_new,180)
    D_len=len(player.Dkangdeck)
    s_len=len(player.show)
    c_len=len(player.cards)         
    if seat==0:
        for i in reversed(range(D_len)):
            for j in reversed(range(3)):
                screen.blit(mjb_new,(290+(mjb_new.get_width()-10)*(3*i+j),screen_height-mjb_new.get_height()-5))
            pic=card_to_image_show(player.Dkangdeck[i][0])
            screen.blit(pic,(290+4+(pic.get_width()-10)*(3*i+1),screen_height-pic.get_height()-5-7))
        for i in reversed(range(s_len)):
            for j in reversed(range(3)):
                pic=card_to_image_show(player.show[i][j])
                screen.blit(pic,(290+(pic.get_width()-10)*(3*i+j+D_len*3),screen_height-pic.get_height()-5))
            if len(player.show[i])==4:
                pic=card_to_image_show(player.show[i][0])
                screen.blit(pic,(290+4+(pic.get_width()-10)*(3*i+1+D_len*3),screen_height-pic.get_height()-5-7))
        if status:
            for i in range(c_len-1):
                pic=card_to_image(player.cards[i])
                screen.blit(pic,(300+(pic.get_width()-10)*(i+s_len*3+D_len*3),screen_height-pic.get_height()-10))
            pic=card_to_image(player.cards[-1])
            screen.blit(pic,(860,screen_height-pic.get_height()-10))
        else:
            for i in range(c_len):
                pic=card_to_image(player.cards[i])
                screen.blit(pic,(300+(pic.get_width()-10)*(i+s_len*3+D_len*3),screen_height-pic.get_height()-10))
        for i in range(len(player.flowerdeck)):
            pic=card_to_image(player.flowerdeck[i])
            pic=pygame.transform.scale(pic,(40,48))
            screen.blit(pic,(300+(pic.get_width()-7)*(i),screen_height-48-53-15))
        
        
    elif seat==2:
        for i in range(D_len):
            for j in range(3):
                screen.blit(mjb_new,(820-(mjb_new.get_width()-10)*(i*3+j),mjb_new.get_height()+40))
            screen.blit(mjb_new,(820+7-(mjb_new.get_width()-10)*(3*i+1),mjb_new.get_height()+40-9))
        for i in reversed(range(s_len)):
            for j in range(3):
                pic=card_to_image(player.show[i][j])
                pic=pygame.transform.rotate(pic,180)
                screen.blit(pic,(820-(pic.get_width()-10)*(i*3+j+D_len*3),pic.get_height()+40))
            if len(player.show[i])==4:
                pic=card_to_image(player.show[i][0])
                pic=pygame.transform.rotate(pic,180)
                screen.blit(pic,(820-(pic.get_width()-10)*(i*3+1+D_len*3)+7,pic.get_height()+40-9))
        for i in range(c_len):
            pic=card_to_image(player.cards[i])
            pic=pygame.transform.rotate(pic,180)
            screen.blit(pic,(810-(pic.get_width()-10)*(i+s_len*3+D_len*3),pic.get_height()+40))
        for i in range(len(player.flowerdeck)):
            pic=card_to_image(player.flowerdeck[i])
            pic=pygame.transform.scale(pic,(40,48))
            pic=pygame.transform.rotate(pic,180)
            screen.blit(pic,(810-(pic.get_width()-7)*(i),53+48+50+5))
    elif seat== 1:
        mjb_new=pygame.transform.rotate(mjb_new,270)
        for i in range(D_len):
            for j in range(3):
                
                screen.blit(mjb_new,(1200-mjb_new.get_width()-20,570-(mjb_new.get_height()-10)*(i*3+j)))
            screen.blit(mjb_new,(1200-mjb_new.get_width()-20+9,570+5-(mjb_new.get_height()-10)*(i*3+1)))
        for i in range(s_len):
            for j in range(3):
                pic=card_to_image(player.show[i][j])
                pic=pygame.transform.rotate(pic,90)
                screen.blit(pic,(1200-pic.get_width()-20,570-(pic.get_height()-10)*(i*3+j+D_len*3)))
            if len(player.show[i])==4:
                pic=card_to_image(player.show[i][0])
                pic=pygame.transform.rotate(pic,90)
                screen.blit(pic,(1200-pic.get_width()-20+9,570+5-(pic.get_height()-10)*(i*3+1+D_len*3)))
        for i in range(c_len):
            pic=card_to_image(player.cards[i])
            pic=pygame.transform.rotate(pic,90)
            screen.blit(pic,(1200-pic.get_width()-20,560-(pic.get_height()-10)*(i+s_len*3+D_len*3)))
        for i in range(len(player.flowerdeck)):
            pic=card_to_image(player.flowerdeck[i])
            pic=pygame.transform.scale(pic,(40,48))
            pic=pygame.transform.rotate(pic,90)
            screen.blit(pic,(1200-53-48-25,560-(pic.get_height()-7)*i))
            
    elif seat==3:
        mjb_new=pygame.transform.rotate(mjb_new,90)
        for i in range(D_len):
            for j in range(3):
                
                screen.blit(mjb_new,(20,50+(mjb_new.get_height()-10)*(i*3+j)))
            screen.blit(mjb_new,(20-6,50-3+(mjb_new.get_height()-10)*(i*3+1)))
        for i in range(s_len):
            for j in range(3):
                pic=card_to_image(player.show[i][j])
                pic=pygame.transform.rotate(pic,270)
                screen.blit(pic,(20,50+(pic.get_height()-10)*(i*3+j+D_len*3)))
            if len(player.show[i]) ==4:
                pic=card_to_image(player.show[i][0])
                pic=pygame.transform.rotate(pic,270)
                screen.blit(pic,(20-6,50-3+(pic.get_height()-10)*(i*3+1+D_len*3)))
        for i in range(c_len):
            pic=card_to_image(player.cards[i])
            pic=pygame.transform.rotate(pic,270)
            screen.blit(pic,(20,60+(pic.get_height()-10)*(i+s_len*3+D_len*3)))
        for i in range(len(player.flowerdeck)):
            pic=card_to_image(player.flowerdeck[i])
            pic=pygame.transform.scale(pic,(40,48))
            pic=pygame.transform.rotate(pic,270)
            screen.blit(pic,(53+25,60+(pic.get_height()-7)*i))
def draw_back_cards(players,rot=0):
    mjback_new=pygame.transform.scale(mjback,(44,53))
    mjb_new=pygame.transform.scale(mjb,(44,53))
    
    for i in range(4):
        index=(i+4+rot)%4
        D_len=len(players[index].Dkangdeck)
        s_len=len(players[index].show)
        if i==2:
            mjb_new=pygame.transform.rotate(mjb,180)
            for i in range(D_len):
                for j in range(3):
                    screen.blit(mjb_new,(820-(mjb_new.get_width()-10)*(i*3+j),mjb_new.get_height()+40+10))
                screen.blit(mjb_new,(820+7-(mjb_new.get_width()-10)*(3*i+1),mjb_new.get_height()+40-9+10))
            for i in range(s_len):
                for j in range(3):
                    pic=card_to_image(players[index].show[i][j])
                    pic=pygame.transform.rotate(pic,180)
                    screen.blit(pic,(820-(pic.get_width()-10)*(i*3+j+D_len*3),pic.get_height()+40+10))
                if len(players[index].show[i])==4:
                    pic=card_to_image(players[index].show[i][0])
                    pic=pygame.transform.rotate(pic,180)
                    screen.blit(pic,(820-(pic.get_width()-10)*(i*3+1+D_len*3)+7,pic.get_height()+40-9+10))
            for i in range(len(players[index].flowerdeck)):
                pic=card_to_image(players[index].flowerdeck[i])
                pic=pygame.transform.scale(pic,(40,48))
                pic=pygame.transform.rotate(pic,180)
                screen.blit(pic,(810-(pic.get_width()-7)*(i),53+48+50+5))
            for i in reversed(range(len(players[index].cards))):
                pic=pygame.transform.rotate(mjb_new,180)
                screen.blit(pic,(810-34*(i+3*(s_len+D_len)),pic.get_height()+40))
        elif i==1 :
            mjb_new=pygame.transform.rotate(mjb,90)
            for i in range(D_len):
                for j in range(3):
                    screen.blit(mjb_new,(1200-mjb_new.get_width()-20,570-(mjb_new.get_height()-10)*(i*3+j)))
                screen.blit(mjb_new,(1200-mjb_new.get_width()-20+9,570+5-(mjb_new.get_height()-10)*(i*3+1)))
            for i in range(s_len):
                for j in range(3):
                    pic=card_to_image(players[index].show[i][j])
                    pic=pygame.transform.rotate(pic,90)
                    screen.blit(pic,(1200-pic.get_width()-20,570-(pic.get_height()-10)*(i*3+j+D_len*3)))
                if len(players[index].show[i])==4:
                    pic=card_to_image(players[index].show[i][0])
                    pic=pygame.transform.rotate(pic,90)
                    screen.blit(pic,(1200-pic.get_width()-20+9,570+5-(pic.get_height()-10)*(i*3+1+D_len*3)))
            for i in range(len(players[index].cards)):
                pic=mjback_new
                pic=pygame.transform.rotate(pic,90)
                screen.blit(pic,(1200-pic.get_width()-20,560-(pic.get_height()-9)*(i+3*(s_len+D_len))))
            for i in range(len(players[index].flowerdeck)):
                pic=card_to_image(players[index].flowerdeck[i])
                pic=pygame.transform.scale(pic,(40,48))
                pic=pygame.transform.rotate(pic,90)
                screen.blit(pic,(1200-53-48-25,560-(pic.get_height()-7)*i))
        elif i==3:
            mjb_new=pygame.transform.rotate(mjb,270)
            for i in range(D_len):
                for j in range(3):
                    screen.blit(mjb_new,(20,50+(mjb_new.get_height()-10)*(i*3+j)))
                screen.blit(mjb_new,(20-6,50-3+(mjb_new.get_height()-10)*(i*3+1)))
            for i in range(s_len):
                for j in range(3):
                    pic=card_to_image(players[index].show[i][j])
                    pic=pygame.transform.rotate(pic,270)
                    screen.blit(pic,(20,50+(pic.get_height()-10)*(i*3+j+D_len*3)))
                if len(players[index].show[i]) ==4:
                    pic=card_to_image(players[index].show[i][0])
                    pic=pygame.transform.rotate(pic,270)
                    screen.blit(pic,(20-6,50-3+(pic.get_height()-10)*(i*3+1+D_len*3)))
            for i in range(len(players[index].cards)):
                pic=pygame.transform.rotate(mjback_new,270)
                screen.blit(pic,(20,60+(pic.get_height()-9)*(i+3*(s_len+D_len))))
            for i in range(len(players[index].flowerdeck)):
                pic=card_to_image(players[index].flowerdeck[i])
                pic=pygame.transform.scale(pic,(40,48))
                pic=pygame.transform.rotate(pic,270)
                screen.blit(pic,(53+25,60+(pic.get_height()-7)*i))
def draw_choose_card(players,rot=0,status=True):
    draw_card(players[rot],0,status)
    draw_back_cards(players,rot)

def draw_all_player(players,dir1):
    for i in range(4):
        index=(i+dir1)%4
        draw_card(players[index],i)

def draw_back():
    for i in range(16):
        pic=mjb
        screen.blit(pic,(300+(pic.get_width()-8)*i,pic.get_height()+40))
    for i in range(16):
        pic=mjback
        pic=pygame.transform.rotate(pic,90)
        screen.blit(pic,(1200-pic.get_width()-20,560-(pic.get_height()-9)*i))
    for i in range(16):
        pic=mjback
        pic=pygame.transform.rotate(pic,270)
        screen.blit(pic,(20,60+(pic.get_height()-9)*i))
    for i in range(16):
        pic=mjb
        pic=pygame.transform.rotate(pic,180)
        screen.blit(pic,(810-(pic.get_width()-8)*(i),screen_height-pic.get_height()-10))
def num_to_seat(num):
    if num==0:
        return '???'
    if num==1:
        return '???'
    if num==2:
        return '???'
    if num==3:
        return '???'
def draw_change(player_in,card,player_next):
    pic=card_to_image(card)
    pic=pygame.transform.scale(pic,(88,104))
    screen.blit(pic,(500,430))
    direction_play=num_to_seat(player_in)
    direction_next=num_to_seat(player_next)                
    text_play='%s?????????'%direction_play
    text_next='??????%s???'%direction_next
    text_play=font.render(text_play,50,(0,0,0))
    text_next=font.render(text_next,50,(0,0,0))
    screen.blit(text_play,(320,480))
    screen.blit(text_next,(620,480))
    draw_back()
    pygame.display.update()

def draw_pon_button(card):
    text='???'
    pon=font.render(text,55,(0,0,0))
    screen.blit(buttonb,(420,470))
    screen.blit(pon,(413,479))
    pic=card_to_image_show(card)
    screen.blit(pic,(480,475))
def draw_eat_button():
    text='???'
    eat=font.render(text,55,(0,0,0))
    screen.blit(buttonb,(510,470))
    screen.blit(eat,(500,479))
def draw_kang_button(card):
    text='???'
    bar=font.render(text,55,(0,0,0))
    screen.blit(buttonb,(325,470))
    screen.blit(bar,(318,479))
    pic=card_to_image_show(card)
    screen.blit(pic,(390,475))
def draw_hu_button():
    text='???'
    hu=font.render(text,55,(0,0,0))
    screen.blit(buttonb,(600,470))
    screen.blit(hu,(593,479))
def draw_back_button():
    text='???'
    back=font.render(text,55,(0,0,0))
    screen.blit(buttonb,(720,470))
    screen.blit(back,(727,479))
def click_button(listb=[False,False,False,False]):
    (mousex,mousey)=pygame.mouse.get_pos()
    if 470<=mousey<=530:
        if 330<=mousex<=390 and listb[0]==True:
            return 'k'
        if 420<=mousex<=480 and listb[1]==True:
            return 'p'
        if 510<=mousex<=570 and listb[2]==True:
            return 'e'
        if 600<=mousex<=660 and listb[3]==True:
            return 'h'
        if 720<=mousex<=780:
            return 'n'
    return None
def click_eat(eatdict):
    (mousex,mousey)=pygame.mouse.get_pos()
    if 575<=mousex<=687:
        if 400<=mousey<=453 and eatdict['a']!=None:
            return 'a'
        if 455<=mousey<=508 and eatdict['b']!=None:
            return 'b'
        if 510<=mousey<=563 and eatdict['c']!=None:
            return 'c'
    if 720<=mousex<=780 and 470<=mousey<=530:
            return 'n'
    return None
def draw_eat_choose(eatdict):
    if eatdict['a']!=None:
        for i in reversed (range(3)):
            pic=card_to_image_show(eatdict['a'][i])
            screen.blit(pic,(575+34*i,400))
    if eatdict['b']!=None:
        for i in reversed (range(3)):
            pic=card_to_image_show(eatdict['b'][i])
            screen.blit(pic,(575+34*i,455))
    if eatdict['c']!=None:
        for i in reversed(range(3)):
            pic=card_to_image_show(eatdict['c'][i])
            screen.blit(pic,(575+34*i,510))
def draw_tai(tainum,word,dict1):
    for i in range(len(word)):
        text='%s:%d???'%(word[i],dict1[word[i]])
        text_tai=font.render(text,40,(0,0,0))
        screen.blit(text_tai,(300,170+40*i))
    #tai_sum='??????%d???'%tainum
    #tai_sum=font.render(tai_sum,40,(0,0,0))
    #screen.blit(tai_sum,(400,170+40*len(word)))
def draw_hu(rot,dir1):
    text='%s?????????%s?????????'%(num_to_seat(rot),num_to_seat(dir1))
    text=font.render(text,80,(0,0,0))
    screen.blit(text,(500,500))
def draw_self_hu(rot):
    text='%s?????????'%num_to_seat(rot)
    text=font.render(text,80,(0,0,0))
    screen.blit(text,(560,500))
def flow_game():
    text='??????'
    text=font.render(text,80,(0,0,0))
    screen.blit(text,(560,500))
####setting
sequence=['w','t','s','b']
class card():    
    def __init__(self, ide = None, num = None, color = None):
        self.id = ide
        self.num = num
        if self.id=='f':
            self.color=color
    def __str__(self):
        if self.id=='f':
            return '%s%d%s'%(self.id, self.num, self.color)
        else:
            return '%s%d'%(self.id, self.num)
        
    def __eq__(self,other):
        if self.id==other.id and self.num==other.num:
            return True
        return False
'''======================================================'''
def select_mj(player,status=True):
    (mousex,mousey)=pygame.mouse.get_pos()
    non=card()
    if status: 
        for i in range(len(player.cards)-1):
            x=300+(34)*3*(len(player.show)+len(player.Dkangdeck))+34*i
            y=597
            if x<mousex<=x+34 and y<mousey<y+41:
                select = player.cards[i]
                return select
        if 860<mousex<+894 and y<mousey<y+41:
            select = player.cards[-1]
            return select
    else:
        for i in range(len(player.cards)):
            x=300+(34)*3*(len(player.show)+len(player.Dkangdeck))+34*i
            y=597
            if x<mousex<=x+34 and y<mousey<y+41:
                select = player.cards[i]
                return select
    return non

'''=============='''
class Deck(): 
    ide=['w', 't', 's', 'b', 'f']
    def __init__(self):
        self.cards=[]
        for i in Deck.ide:
            if i == 'f':
                for j in range(1,5):
                    for k in ('b', 'r'):
                        self.cards.append(card(i,j,k))
            elif i=='b':
                for j in range(1,8):
                    self.cards.extend([card(i,j)]*4)
            else:
                for j in range(1,10):
                    self.cards.extend([card(i,j)]*4)     

    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return ' '.join(res)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal_card(self, player1, player2, player3, player4):
        for i in range(4):
            for player in (player1, player2, player3, player4):
                player.cards+=self.cards[:4]
                del self.cards[:4]
    def pop_card(self):
        return self.cards.pop(0)
    def pop_end_card(self):
        return self.cards.pop(-1)
'''============================================================================================================'''

class hand(Deck):
    def __init__(self,direction):#??????????????????????????????
        self.cards=[]      #??????
        self.show=[]       #?????????????????????
        self.draw=True
        self.kang=False
        self.pong=False       
        self.eat=False
        self.flower_hu=False#????????????
        self.flowerdeck=[]  #????????????
        self.Dkangdeck=[]   #???????????????
        self.dir=direction  #????????????

    '''------------------------------------------------------'''    
    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        res.append('show:')
        Ls=[str(card) for cards in self.show for card in cards]
        res.extend(Ls)

        res.append('Dkangdeck:')
        Ld=[str(card) for cards in self.Dkangdeck for card in cards]
        res.extend(Ld)   
                
        res.append('flowerdeck:')
        for card in self.flowerdeck:
            res.append(str(card))   
            
        return ' '.join(res)

    '''------------------------------------------------------'''     
    def play_card(self,status=True):        #??????????????? 
        going=True
        while going:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = e.pos
                    if e.button == 1:
                        selectmj = select_mj(self,status)
                        c=card()
                        if selectmj!=c:
                            going=False
        self.cards.remove(selectmj)
        self.cards.sort(key=lambda card: card.num)
        self.cards.sort(key=lambda card: sequence.index(card.id))
        return selectmj
    '''------------------------------------------------------'''   
    def Flower(self,f_card,init=False):   #??????:?????????????????????(?????????????????????)????????????????????????
        if f_card.id=='f':
            if not init:
                self.cards.append(f_card)
                display_all(game,circle,deck,table)
                draw_seat(game,self.dir)
                draw_choose_card(playerlist,self.dir,True)
                text='??????'
                text=font.render(text,80,(0,0,0))
                screen.blit(text,(560,500))
                pygame.display.update()
                going=True
                time.sleep(1)
                del self.cards[-1]
            self.flowerdeck.append(f_card)
            return True
        else:
            return False
    '''------------------------------------------------------'''       
    def DarkKang(self,Kcard):   #?????????????????????????????????????????????????????????>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        cnt=[]
        for i in reversed(range(len(self.cards))):
            if self.cards[i]==Kcard:
                cnt.append(i)
        if len(cnt)==3:
            self.cards.append(Kcard)
            display_all(game,circle,deck,table)
            draw_seat(game,self.dir)
            draw_choose_card(playerlist,self.dir,True)
            draw_kang_button(Kcard)
            draw_back_button()
            pygame.display.update()
            going=True
            while going:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        (x,y) = e.pos
                        if e.button == 1:
                            select_button = click_button(listb=[True,False,False,False])
                            if select_button!=None:
                                going=False
            if select_button=='k':
                tmplist=[Kcard]
                del self.cards[-1]
                for j in range(len(cnt)):#???self.cards????????????????????????????????????list????????????
                    tmplist.append(self.cards.pop(cnt[j]))
                self.Dkangdeck.append(tmplist)
                return True
            elif select_button=='n' :
                del self.cards[-1]
                return False
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''        
        kang_af_pong=-1
        for k in range(len(self.show)):
            if self.show[k][0]==Kcard and self.show[k][1]==Kcard:
                kang_af_pong=k
                break
        if kang_af_pong !=-1:
            self.kang=True
            self.cards.append(Kcard)
            #==>??????????????????????????????
            display_all(game,circle,deck,table)
            draw_seat(game,self.dir)
            draw_choose_card(playerlist,self.dir,True)
            draw_kang_button(Kcard)
            draw_back_button()
            pygame.display.update()
            going=True
            while going:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        (x,y) = e.pos
                        if e.button == 1:
                            select_button = click_button(listb=[True,False,False,False])
                            if select_button!=None:
                                going=False
            if select_button=='k':
                del self.cards[-1]
                self.show[kang_af_pong].append(Kcard)
                self.kang=False
                return True
            if select_button=='n':
                del self.cards[-1]
                self.kang=False
                return False                
        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''        
        return False
    '''------------------------------------------------------'''               
    def Draw(self,flag1=False, flag2=False): #???????????????????????????????????????????????????????????????
        card_d=card()
        check=self.draw
        while self.draw:
            card_d=deck.pop_card()
            flag1=self.Flower(card_d)#????????????
            flag2=self.DarkKang(card_d)#????????????
            self.draw=flag1 or flag2
            if self.draw:               
                self.flower_hu=True     
            
            if not self.draw:  #????????????????????????
                self.cards.append(card_d)
        self.draw=True
        return check
    '''------------------------------------------------------'''        
    def DarkKang_2(self): #??????: ???????????????????????????????????????????????????????????????
        while True:
            num=-1
            leng=len(self.cards)-5
            while num<leng:
                leng=len(self.cards)-5
                num+=1
                if self.cards[num]==self.cards[num+1] and self.cards[num]==self.cards[num+2] and self.cards[num]==self.cards[num+3]:
                    #==>??????????????????draw_kang Draw_back
                    display_all(game,circle,deck,table)
                    draw_seat(game,self.dir)
                    draw_choose_card(playerlist,self.dir,True)
                    draw_kang_button(self.cards[num])
                    draw_back_button()
                    pygame.display.update()
                    going=True
                    while going:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                pygame.quit()
                            if e.type == pygame.MOUSEBUTTONDOWN:
                                (x,y) = e.pos
                                if e.button == 1:
                                    select_button = click_button(listb=[True,False,False,False])
                                    if select_button!=None:
                                        going=False
                    if select_button=='k':
                        tmplist=[self.cards[num]]*4
                        for i in range(4):
                            #??????????????????????????????
                            del self.cards[num]
                            #===>??????????????????????????????  Dkangdeck  ???(?????????????????????????????????????????????)
                        self.Dkangdeck.append(tmplist)
                        while True:#??????????????????
                            card_d=deck.pop_end_card()
                            flag1=self.Flower(card_d)#????????????
                            flag2=self.DarkKang(card_d)#???????????????????????????????????????
                            Bool=flag1 or flag2
                            if not Bool:  #????????????????????????
                                self.cards.append(card_d)
                                self.cards.sort(key=lambda card: card.num) 
                                self.cards.sort(key=lambda card: sequence.index(card.id))
                                break  
            break
    '''------------------------------------------------------'''           
    
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    def Eat_or_Pong(self, other, e_card, flag1=False,flag2=False): #???????????????????????????
        seq=[-1,-1,-1,-1]
        for ide in ('t', 'w', 's'):
            if e_card.id==ide:
                
                for i in range(len(self.cards)):
                    if self.cards[i].id==ide and self.cards[i].num==e_card.num-2:
                        seq[0]=i
                    if self.cards[i].id==ide and self.cards[i].num==e_card.num-1:
                        seq[1]=i
                    if self.cards[i].id==ide and self.cards[i].num==e_card.num+1:
                        seq[2]=i
                    if self.cards[i].id==ide and self.cards[i].num==e_card.num+2:
                        seq[3]=i                                        
        eatdict={'a':None, 'b':None, 'c':None}
        if seq[0]!=-1 and seq[1]!=-1:
            eatdict['a']=[self.cards[seq[0]], e_card, self.cards[seq[1]]]         
        if seq[1]!=-1 and seq[2]!=-1:
            eatdict['b']=[self.cards[seq[1]], e_card, self.cards[seq[2]]]        
        if seq[2]!=-1 and seq[3]!=-1:
            eatdict['c']=[self.cards[seq[2]], e_card, self.cards[seq[3]]]
        #??????????????????
        if any(eatdict[key]!=None for key in eatdict.keys()):
            self.eat=True
        #??????????????????
        cnt=[]
        for i in reversed(range(len(self.cards))):
            if self.cards[i]==throwcard:
                cnt.append(i)
                if len(cnt)==2:
                    break
        if len(cnt)==2:
            self.pong=True
        #>>>>>>>>>>>>>>>>>>>>??????class???attribute?????????
        if self.eat or self.pong:
            display_all(game,circle,deck,table)
            draw_seat(game,self.dir)
            draw_choose_card(playerlist,self.dir,False)
            if self.eat:
                draw_eat_button() 
            if self.pong:
                draw_pon_button(e_card)
            draw_back_button()
            pygame.display.update()
            going=True
            while going:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        if e.button == 1:
                            select_button = click_button([False,self.pong,self.eat,False])
                            if select_button!=None:
                                going=False
            if select_button=='p':
                self.Pong(cnt,e_card)
                self.draw=False
                self.eat=False
                self.pong=False
                self.kang=False
                return card(),False

            elif select_button=='e':
                display_all(game,circle,deck,table)
                draw_seat(game,self.dir)
                draw_choose_card(playerlist,self.dir,False)
                draw_eat_button() 
                draw_back_button()
                draw_eat_choose(eatdict)
                pygame.display.update()
                going=True
                while going:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                        if e.type == pygame.MOUSEBUTTONDOWN:
                            (x,y) = e.pos
                            if e.button == 1:
                                select_eat = click_eat(eatdict)
                                if select_eat!=None:
                                    going=False
                #==>????????????????????????????????????
                if select_eat=='n':
                    self.draw=True
                    self.pong=False
                    self.eat=False
                    return e_card,True
                elif select_eat=='a':
                    self.show.append(eatdict['a'])
                    del self.cards[seq[1]]
                    del self.cards[seq[0]]#==>??????????????????????????????show??????
                    self.eat=False
                    self.draw=False
                    self.pong=False
                    self.kang=False
                    return card(),False
                
                elif select_eat=='b':
                    self.show.append(eatdict['b'])
                    del self.cards[seq[2]]
                    del self.cards[seq[1]]
                    self.eat=False                        
                    self.draw=False
                    self.pong=False
                    self.kang=False                        
                    return card(),False
                
                elif select_eat=='c':
                    self.show.append(eatdict['c'])
                    del self.cards[seq[3]]
                    del self.cards[seq[2]]
                    self.eat=False
                    self.draw=False
                    self.pong=False
                    self.kang=False                        
                    return card(),False
            elif select_button=='n':
                self.draw=True
                self.eat=False
                self.pong=False
                return e_card ,True       
        '''~~~~~~~~~~~~~~~~~~~~~??????????????????~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        return e_card,True
          
    '''===============================??????????????????code==================================='''
    
    '''------------------------------------------------------'''
    
    def BrightKang(self,cnt,t_card):
        tmplist=[t_card]
        for i in cnt:
            tmplist.append(self.cards.pop(i))
        self.show.append(tmplist)
    '''------------------------------------------------------'''            
    def Pong(self,cnt,t_card):
        tmplist=[t_card]
        for i in cnt:
            tmplist.append(self.cards.pop(i))
        self.show.append(tmplist)

#setting



def ChangeRotation(rot, next_p):#??????????????? ??? ????????????
    if next_p!=-2:
        rot=next_p
        next_p=-2
    else:
        rot+=1
        if rot>=4:
            rot-=4
    return rot, next_p
'''================================================================================='''
def Pong_or_Kang(throwcard,rot):#??????????????????????????????????????????or ???
    next_p=-2
    canpong=-1#???????????????/??????????????????
    for p in range(len(playerlist)):
        if p!=rot and p!=(rot+1)%4:#???????????????????????????
            cnt=[]
            for i in reversed(range(len(playerlist[p].cards))):
                if playerlist[p].cards[i]==throwcard:
                    cnt.append(i)
            if len(cnt)>=2 :
                canpong=p #?????????????????????????????????######
                draw_background()
                draw_top(game,circle,deck)
                draw_change(rot,throwcard,p)
                pygame.display.update()
                going=True
                while going:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                        if e.type == pygame.MOUSEBUTTONDOWN:
                            if e.button == 1:
                                going=False
                #print('?????? %s ,??????????????????' %playerdict[p])
                #======================================>???????????????????????????
                break  #???????????????????????????????????????
    if len(cnt)==3:#???????????????????????????
        playerlist[canpong].kang=True
        playerlist[canpong].pong=True
        #inp=input('????????????????(k/p/n)%s' %throwcard)#
        display_all(game,circle,deck,table)
        draw_seat(game,canpong)
        draw_choose_card(playerlist,canpong,False)
        draw_pon_button(throwcard)
        draw_kang_button(throwcard)
        draw_back_button()
        pygame.display.update()
        going=True
        while going:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = e.pos
                    if e.button == 1:
                        select_button = click_button([True,True,False,False])
                        if select_button!=None:
                            going=False
        if select_button=='k':
            playerlist[canpong].BrightKang(cnt,throwcard)#??????()
            throwcard=card()
            next_p=canpong
            playerlist[canpong].kang=False
            playerlist[canpong].pong=False
            return throwcard, next_p ,True
        if select_button =='p':#######select_button(return 'p')
            playerlist[canpong].Pong(cnt,throwcard)#???()
            throwcard=card()
            next_p=canpong
            playerlist[canpong].kang=False
            playerlist[canpong].pong=False
            playerlist[canpong].draw=False
            return throwcard, next_p ,False
        elif select_button=='n':#######select_button(return 'n')
            playerlist[canpong].kang=False
            playerlist[canpong].pong=False
            next_p=-2
            return throwcard, next_p ,True            

    elif len(cnt)==2:
        playerlist[canpong].pong=True
        #inp=input('??????????(p/n)%s' %throwcard)
        display_all(game,circle,deck,table)
        draw_seat(game,canpong)
        draw_choose_card(playerlist,canpong,False)
        draw_pon_button(throwcard)
        draw_back_button()
        pygame.display.update()
        going=True
        while going:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = e.pos
                    if e.button == 1:
                        select_button = click_button([False,True,False,False])
                        if select_button!=None:
                            going=False
        if select_button=='p':#######select_button(return 'p')
            playerlist[canpong].Pong(cnt,throwcard)#???()
            playerlist[canpong].pong=False
            playerlist[canpong].draw=False
            throwcard=card()
            next_p=canpong
            return throwcard, next_p ,False
            
        if select_button=='n':#######select_button(return 'n')
            playerlist[canpong].pong=False
            #??????????????????throwcard?????????????????????????????????????????????
            next_p=-2
            return throwcard, next_p ,True
    return throwcard, next_p ,False         
   

'''=================================================================================='''
def diu_pai(playerlist,rot,throwcard):   #???player??????playerlist??#??????????????????rot?????????
    for player in playerlist:#player_list:#??????????????????
        if player!=playerlist[rot]:
            tmplist=copy.deepcopy(player.cards)
            tmplist.append(throwcard)
            list_hu=hu_pai(tmplist,player.show,player.Dkangdeck,circle,player.dir,player.flowerdeck,False,game)#(True?????????,False?????????)
            if list_hu[0]:
                display_all(game,circle,deck,table)
                draw_change(rot,throwcard,player.dir)
                going=True
                while going:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                        if e.type == pygame.MOUSEBUTTONDOWN:
                            if e.button == 1:
                                going=False
                #inp=input('????(y/n)' )#######
                player.cards.append(throwcard)
                display_all(game,circle,deck,table)
                draw_seat(game,player.dir)
                draw_choose_card(playerlist,player.dir,True)
                draw_hu_button()
                draw_back_button()
                pygame.display.update()
                going=True
                while going:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                        if e.type == pygame.MOUSEBUTTONDOWN:
                            (x,y) = e.pos
                            if e.button == 1:
                                select_button = click_button([False,False,False,True])
                                if select_button!=None:
                                    going=False
                if select_button=='h':#######select_button(return 'h')
                    flag=False
                    win_flag=1
                    #??????????????????????????????????????????????????????????????????#####
                    display_all(game,circle,deck,table)
                    draw_hu(rot,player.dir) 
                    draw_all_player(playerlist,player.dir) 
                    draw_seat(game,player.dir)
                    pygame.display.update()
                    going=True
                    while going:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                pygame.quit()
                            if e.type == pygame.MOUSEBUTTONDOWN:
                                if e.button == 1:
                                    going=False
                    draw_background()
                    draw_tai(list_hu[1],list_hu[2],list_hu[3])
                    '''
                    for w in list_hu[2]:
                        #???????????????????????????????????????
                        print(w,list_hu[3][w],'???\n')
                        #?????????????????????
                    '''
                    if player.dir==j:#??????????????????
                        flag=True#??????????????????True
                        #print('??????',zhuang,'???\n')
                        text_z='??????:%d???'%zhuang
                        text_z=font.render(text_z,40,(0,0,0))
                        screen.blit(text_z,(300,170+40*len(list_hu[2])))
                        list_hu[1]+=1
                        
                    elif rot==j:
                        text_z='??????:%d???'%zhuang
                        text_z=font.render(text_z,40,(0,0,0))
                        screen.blit(text_z,(300,170+40*len(list_hu[2])))
                        list_hu[1]+=1
                    elif len(list_hu[2])==0:
                        text='??????:0???'
                        text=font.render(text,40,(0,0,0))
                        screen.blit(text,(300,170))
                    moneylist[playerlist.index(player)]+=(100+50*list_hu[1])
                    moneylist[rot]-=(100+50*list_hu[1])
                    for i in range(4):
                        text_money='%s?????????:%d'%(num_to_seat(i),moneylist[i])
                        text_money=font.render(text_money,40,(0,0,0))
                        screen.blit(text_money,(500,200+50*i))
                    pygame.display.update()
                    going=True
                    while going:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                pygame.quit()
                            if e.type == pygame.MOUSEBUTTONDOWN:
                                if e.button == 1:
                                    going=False
                    return 1,list_hu[1],player.dir,flag
                    
                elif select_button=='n':#######select_button(return 'n')
                     player.cards.pop(-1)
            else:
                continue
                #??????????????????
    return 0,0,rot,False
'''==================================================================================='''
def mo_pai(player):
    list_hu=hu_pai(player.cards,player.show,player.Dkangdeck,circle,player.dir,player.flowerdeck,True,game)
    if list_hu[0]:
        #?????????????????????
        display_all(game,circle,deck,table)
        draw_seat(game,player.dir)
        draw_choose_card(playerlist,player.dir,True)
        draw_hu_button()
        draw_back_button()
        pygame.display.update()
        #inp=input('????(y/n)' )
        going=True
        while going:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        select_button = click_button([False,False,False,True])
                        if select_button!=None:
                            going=False
        if select_button=='h':
            win_flag=1
            flag=False
            draw_seat(game,player.dir)
            display_all(game,circle,deck,table)
            draw_all_player(playerlist,player.dir)
            draw_self_hu(player.dir)
            pygame.display.update()
            #??????????????????????????????????????????????????????????????????
            going=True
            while going:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        if e.button == 1:
                            going=False
            draw_background()
            draw_tai(list_hu[1],list_hu[2],list_hu[3])
            '''
            for w in list_hu[2]:
                #???????????????????????????????????????
                print(w,list_hu[3][w],'???\n')
                #?????????????????????
                '''
            if player.dir==j:#??????????????????
                flag=True#??????????????????True
                text_z='??????:%d???'%zhuang
                text_z=font.render(text_z,40,(0,0,0))
                screen.blit(text_z,(300,170+40*len(list_hu[2])))
                #print('??????',zhuang,'???\n')
                list_hu[1]+=zhuang
                moneylist[playerlist.index(player)]+=((100+50*list_hu[1])*3)
                for i in range(len(playerlist)):
                    if i==playerlist.index(player):
                        continue
                    else:
                        moneylist[i]-=(100+50*list_hu[1])
                #??????????????? break
            else:#???????????????
                text_z='??????:%d???'%zhuang
                text_z=font.render(text_z,40,(0,0,0))
                screen.blit(text_z,(300,170+40*len(list_hu[2])))
                #print('??????',zhuang,'???\n')
                #??????????????? break
                list_hu[1]+=zhuang
                moneylist[playerlist.index(player)]+=((100+50*list_hu[1])*3-100)
                for i in range(len(playerlist)):
                    if i==playerlist.index(player):
                        continue
                    elif i==game:
                        moneylist[i]-=(100+50*list_hu[1])
                    else:
                        moneylist[i]-=(100+50*(list_hu[1]-1))
            for i in range(4):
                text_money='%s?????????:%d'%(num_to_seat(i),moneylist[i])
                text_money=font.render(text_money,40,(0,0,0))
                screen.blit(text_money,(500,200+50*i))
            pygame.display.update()
            going=True
            while going:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        if e.button == 1:
                            going=False
            return 1,list_hu[1],player.dir,flag
    return 0,0,player.dir,False
                        
import copy
'''======================================================================================='''                       

def tai(show,paishape,kang,pai,circle,direction,flower,boolean,wind):
    dict1={'?????????':4,'??????':1,'??????':1,'?????????':8,'?????????':4,'?????????':16,'?????????':8,'?????????':8,'?????????':4,'?????????':2,'?????????':5,'?????????':8,'??????':1,'?????????':1,'??????':1,'?????????':8,'??????':1,'??????':1,'???????????????':3,'??????':1,'??????':1}
    duinum=0
    shunnum=0
    word=[]
    tainum=0
    shi=0
    shi_1=0
    yuan=0
    yuan_1=0
    w=0
    s=0
    t=0
    b=0
    Dong=[]
    paishape2=copy.deepcopy(paishape)
    paishape.extend(show)
    paishape.extend(kang)
    for shape in paishape:
        if shape[0].id=='w':
            w+=1
        elif shape[0].id=='t':
            t+=1
        elif shape[0].id=='s':
            s+=1
        elif shape[0].id=='b':
            b+=1
    if w and s==0 and t==0 and b==0:
        word.append('?????????')
    elif s and w==0 and t==0 and b==0:
        word.append('?????????')
    elif t and w==0 and s==0 and b==0:
        word.append('?????????')
    elif b and w==0 and t==0 and s==0:
        word.append('?????????')
    elif s and w==0 and t==0 :
        word.append('?????????')
    elif t and s==0 and t==0:
        word.append('?????????')
    elif w and t==0 and s==0:
        word.append('?????????')
    for x in paishape2:
        if len(x)==3:
            if x[0].num==x[1].num:
                duinum+=1
    duinum+=len(kang)
    painum=0
    flag=0
    if not(boolean):
        for shape in paishape2:
            count=0
            for mj in shape:
                if mj.num==pai.num and mj.id==pai.id:
                    painum+=1
                    count+=1
            if count==3:
                flag=1
                duinum-=1
   # if painum>=2 and flag:
     #   duinum+=1
    if duinum==3:
        word.append('?????????')
    elif duinum==4:
        word.append('?????????')
    elif duinum==5:
        word.append('?????????')
    duinum=0
    for x in paishape:
        if len(x)>=3:
            if x[0].num==x[1].num:
                duinum+=1
            else:
                shunnum+=1
    if shunnum==0:
        word.append('?????????')
    for shape in paishape:
        if len(shape)>=3:
            if shape[0].id=='b' and 5<=shape[0].num<=7:
                word.append('?????????')
                yuan+=1
            elif shape[0].id=='b' and shape[0].num==direction+1:
                word.append('??????')
                shi+=1
            elif shape[0].id=='b' and 1<=shape[0].num<=4:
                shi+=1
        else:
            if shape[0].id=='b' and 5<=shape[0].num<=7:
                yuan_1+=1
            elif shape[0].id=='b' and 1<=shape[0].num<=4:
                shi_1+=1
    for shape in paishape:
        if len(shape)>=3:
            if shape[0].id=='b' and shape[0].num==circle+1:
                word.append('??????')
                break
    if yuan==3:
        for i in range(3):
            word.remove('?????????')
        word.append('?????????')
    elif yuan==2 and yuan_1==1:
        for i in range(2):
            word.remove('?????????')
        word.append('?????????')
    for shape in paishape2:
        for mj in shape:
            if mj.id==pai.id and mj.num==pai.num :
                Dong.append(shape)
                break
    if shi==4:
        word.remove('??????')
        word.remove('??????')
        word.append('?????????')
    elif shi==3 and shi_1==1:
        if '??????' in word:
            word.remove('??????')
        word.remove('??????')
        word.append('?????????')
    count=0
    for shape in Dong:
        shape=sorted(shape,key=lambda x:x.num)
        if not(shape[0].num==pai.num-1):
            count=0
            break
        else:
            count=1
    if count:
        word.append('??????')
    count=0
    if pai.num==3 and not(pai.id=='b'):
        for shape in Dong:
            shape=sorted(shape,key=lambda x:x.num)
            if not(shape[1].num==pai.num-1) or not(shape[0].num==pai.num-2):
                count=0
                break
            else:
                count=1
    if count:
        word.append('??????')
    count=0
    if pai.num==7 and not(pai.id=='b'):
        for shape in Dong:
            shape=sorted(shape,key=lambda x:x.num)
            if not(shape[1].num==pai.num+1) or not(shape[2].num==pai.num+2):
                count=0
                break
            else:
                count=1
    if count:
        word.append('??????')
    
    count=0
    countflag=0
    for shape in paishape2:
        if len(shape)==2 and not('??????' in word) and not('??????' in word) and shape[0]==pai:
            for shape in paishape2:
                shape=sorted(shape,key=lambda x:x.num)
                if (shape[0].num==pai.num+1 and shape[0].id==pai.id and shape[1].num==pai.num+2) or (shape[0].num==pai.num-3 and shape[0].id==pai.id and shape[1].num==pai.num-2):
                    countflag=1
            count=1
            break
    if count and not(countflag):
        word.append('??????')
        
    if boolean:
        word.append('??????')
    if len(show)==0:
        if boolean:
            word.append('???????????????')
            word.remove('??????')
        else:
            word.append('??????')
    for mj in flower:
        if mj.num==(direction-game+4+1)%4:
            word.append('??????')
    for w in word:
        tainum+=dict1[w]
    return tainum,word,dict1
'''==============================================================================='''
def hu_pai(list_mj,show,kang,circle,direction,flower,boolean,wind):
    wan=[]
    sol=[]
    ton=[]
    big=[]
    paishape2=[]
    paishape=[]
    last_mj=list_mj[-1]
    for mj in list_mj:
        if mj.id=='w':
            wan.append(mj)
        elif mj.id=='s':
            sol.append(mj)
        elif mj.id=='t':
            ton.append(mj)
        elif mj.id=='b':
            big.append(mj)
#????????????
    list_big=[wan,sol,ton,big]
    one=0
    two=0
    three=0
    for identity in list_big:
        if len(identity)%3==2:
            two+=1
        elif len(identity)%3==0:
            three+=1
        else:
            one+=1
#??????????????????????????????????????????:???????????????????????????????????????????????????
    def check_shun(list1):
        num1=False
        num2=False
        cnt=[]
        list2=copy.deepcopy(list1)
        for i in range(1,len(list1)):
            if int(list1[i].num)==int(list1[0].num)+1 and num1==False:
                num1=True
                cnt.append(i)
            elif int(list1[i].num)==int(list1[0].num)+2 and num2==False:
                num2=True
                cnt.append(i)
                break
        if num1 and num2:
            shape=copy.deepcopy([list2[0],list2[cnt[0]],list2[cnt[1]]])
            paishape.append(shape)
            list2.pop(cnt[1])
            list2.pop(cnt[0])
            list2.pop(0)
            return check_hu2(list2)
        else:
            return False
#???????????????????????????????????????????????????check_hu2??????return False ???check1??????????????????
    def check_hu_bigword(list1):
        list1=sorted(list1,key=lambda x:x.num)
        dui={}
        if len(list1)%3==0:
            for i in range(len(list1)):
                dui[list1[i].num]=dui.get(list1[i].num,0)+1
            for key in dui.keys():
                if not(dui[key]==3):
                    return False
            for i in range(0,len(list1),3):
                shape=[]
                for j in range(3):
                    shape.append(list1[i])
                paishape.append(shape)
            return True
        elif len(list1)%3==2:
            for i in range(len(list1)):
                dui[list1[i].num]=dui.get(list1[i].num,0)+1
            count=0
            for key in dui.keys():
                if dui[key]==2:
                    count+=1
                elif not(dui[key]==3):
                    return False
            if count==1:
                shape=[]
                for x in list1:
                    if dui[x.num]==2:
                        shape.append(x)
                        shape.append(x)
                        list1=list(filter(lambda x:not(dui[x.num]==2),list1))
                        break
                paishape.append(shape)
                for i in range(0,len(list1),3):
                    shape=[]
                    for j in range(3):
                        shape.append(list1[i])
                    paishape.append(shape)
                return True
            else:
                return False
#????????????????????????????????????????????????3????????????????????????????????????3??????????????????2???????????????????????????2???????????????0
    def check_hu2(list1):
        if len(list1)==0:
            return True
        elif len(list1)<3:
            return False
        else:
            if list1[0].num==list1[1].num and list1[0].num==list1[2].num:
                x=copy.deepcopy(list1[0:3])
                paishape.append(x)
                return check_hu2(list1[3:])
            else:
                if (check_shun(list1)):
                    return True
                else:
                    return False
#????????????0?????????????????????????????????????????????????????????????????????????????????
    def check_hu1(list1):
        list1=sorted(list1,key=lambda x:x.num)
        if (len(list1)%3)==2:
            jan={}
            janpai=[]
            janpai2=[]
            for i in range(len(list1)):
                jan[list1[i].num]=jan.get(list1[i].num,0)+1
            janpai=list(jan)
            janpai=list(filter(lambda x:jan[x]>=2,janpai))
            for i in janpai:
                for j in list1:
                    if j.num ==i:
                        janpai2.append(j)
                        break
            for mj in janpai2:
                paishape.clear()
                count=0
                cnt=[]
                shape=[]
                list2=copy.deepcopy(list1)
                for i in range(len(list2)):
                    if list2[i].num==mj.num and count<2:
                        count+=1
                        cnt.append(i)
                for i in range(len(cnt)):
                    shape.append(list2[cnt[i]])
                paishape.append(shape)
                list2.pop(cnt[1])
                list2.pop(cnt[0])
                if check_hu2(list2):
                    return True
                else:
                    paishape.clear()
            return False
        elif (len(list1)%3)==0:
            paishape.clear()
            if (check_hu2(list1)):
                return True
            else:
                return False       
#???????????????????????????????????????(?????????)
    if two==1 and three==3:
        for i in range(len(list_big)-1):
            list_small=list_big[i]
            if not(check_hu1(list_small)):
                return [False,0]
            else:
                paishape2.extend(paishape)
                paishape.clear()
        if check_hu_bigword(list_big[3]):
            paishape2.extend(paishape)
            paishape.clear()
            tai1,word,dict1=tai(show,paishape2,kang,last_mj,circle,direction,flower,boolean,wind)
            return [True,tai1,word,dict1]
        else:
            return [False,0,[],{}]
    else:
        return [False,0,[],{}]
'''===========================??????????????????========================'''

'''==============================draw============================'''

'''=============================circle_to_word==================='''    
moneylist=[5000,5000,5000,5000]         
for i in range(4):#?????????
    circle=i      #??????
    for j in range(4):#?????????
    #????????????       
        game=j
        zhuang=-1
        while True:
        #???????????? ????????????+2
            rot=j
            status=True
            win_flag=0
            zhuang+=2
            zhuang_flag=False
            '''????????????????????????'''
            table=hand(-2)  #'''??????'''
            player_n=hand(3) #'''??????'''
            player_e=hand(0)
            player_w=hand(2)
            player_s=hand(1)
            deck=Deck()   #'''??????'''
            deck.shuffle()#'''??????'''
            #=====================>????????????(?????????~~)

            deck.deal_card(player_n,player_w,player_s,player_e)#'''??????'''
            playerlist=[player_e, player_s, player_w, player_n]
                           #???????????????(0~3)
            
            next_p=-2           #???????????????(????????????)???????????????????????????????????????()
            throwcard=card()    #?????????????????????????????????

            playerlist=[player_e,player_s,player_w,player_n]    
            playerdict={0:'???',1:'???',2:'???',3:'???', 4:'???',-1:'???'}

            for player in playerlist:
                i=0
                while i<len(player.cards):
                    if player.Flower(player.cards[i],True):
                        del player.cards[i]
                        player.cards.append(deck.pop_end_card())
                        i-=1
                    i+=1
                player.cards.sort(key=lambda card: card.num)
                player.cards.sort(key=lambda card: sequence.index(card.id))
            draw_background()
            draw_start_player(game)
            draw_top(circle,game,deck)
            pygame.display.update()
            going=True
            while going:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        if e.button == 1:
                            going=False   
            while True:#????????????
                #======================>??????????????????...(???)??????      
                c=card()  #??????card, ???????????????????????????(throwcard)?????????(?????????or ???????????????/?????????)
                
                if throwcard!=c: #????????????????????????????????????==>??????????????????
                    throwcard,status=playerlist[rot].Eat_or_Pong(playerlist[rot-1], throwcard)

                if throwcard!=c:#??????????????????????????????????????????==>???????????????  table  ???
                    table.cards.append(throwcard)
                    throwcard=c

                status=playerlist[rot].Draw()        
                playerlist[rot].DarkKang_2()#????????????????????????????????????(???????????????????????????)????????????????????????
                #????????????(?????????)
                boolean,hu_tai,direction,zhuang_flag=mo_pai(playerlist[rot])#????????????,??????,?????????????????????
                if boolean:
                    break
                display_all(game,circle,deck,table)
                draw_seat(game,rot)
                draw_choose_card(playerlist,rot,status)
                pygame.display.update()
                throwcard=playerlist[rot].play_card(status)
                boolean1,tai1,direction,zhuang_flag=diu_pai(playerlist,rot,throwcard)#?????????????????????????????? ????????????,??????,?????????????????????
                if boolean1:
                    #print('??????', playerdict[direction], '??????!')
                    break
                
                throwcard, next_p ,status=Pong_or_Kang(throwcard,rot)
                if next_p!=-2:
                    rot =next_p
                
                if len(deck.cards)<=16:
                    display_all(game,circle,deck,table)
                    draw_seat(game,rot)
                    draw_choose_card(playerlist,rot,False)
                    flow_game()
                    pygame.display.update()
                    going=True
                    while going:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                pygame.quit()
                            if e.type == pygame.MOUSEBUTTONDOWN:
                                if e.button == 1:
                                    going=False
                    #============================>??????????????????
                    zhuang_flag=True#???????????? ???????????????
                    break    

                rot, next_p=ChangeRotation(rot,next_p)

                if throwcard!=c:#??????????????????????????????????????????????????????
                    display_all(game,circle,deck,table)
                    pre=(rot-1+4)%4
                    draw_change(pre,throwcard,rot)
                    going=True
                    while going:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                pygame.quit()
                            if e.type == pygame.MOUSEBUTTONDOWN:
                                if e.button == 1:
                                    going=False
                
            #???????????????????????????True ????????????????????? ??????break
            if not(zhuang_flag):
                break
pygame.quit()
