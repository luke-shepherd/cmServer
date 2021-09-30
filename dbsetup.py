#see climbs/models.py

jtree = Places(
id='joshua-tree',
img='./images/joshua-tree-map.jpg',
width=4000,
height=2987
)

trock = Areas(
id='trashcan-rock', 
place=jtree, 
img='images/joshua-tree/trashcan-rock/trashcan-rock-map.jpg',
preview='images/joshua-tree/trashcan-rock/trashcan-rock-preview.jpg',
width=3000,
height=2400,
coords=[1450, 1320, 1580, 1450]
)

forgottenBoulders = Boulders(
id='forgotten-boulders', 
area=trock,
images=["./images/joshua-tree/trashcan-rock/forgotten-boulders/forgotten-boulders-a.jpg", "./images/joshua-tree/trashcan-rock/forgotten-boulders/forgotten-boulders-b.jpg", "./images/joshua-tree/trashcan-rock/forgotten-boulders/forgotten-boulders-c.jpg"],
preview='./images/joshua-tree/trashcan-rock/forgotten-boulders/forgotten-boulders-preview.jpg',
minimap='./images/joshua-tree/trashcan-rock/forgotten-boulders/forgotten-boulders-minimap.jpg',
width=3000, 
height=2000,
coords=[500, 460, 620, 580]
)

crackToJugsClimb = Climbs(
id='crack-to-jugs',
boulder=forgottenBoulders,
grade=0,
stars=0,
height=13,
description=None,
preview='./images/joshua-tree/trashcan-rock/forgotten-boulders/crack-to-jugs/crack-to-jugs-preview.jpg',
imgidx=2,
points=[50, 20, 30, 200, 100, 500, 95, 600],
coords=[1000, 600, 1200, 1250]
)