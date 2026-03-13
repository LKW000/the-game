# 🕹️ Coin Collector 
A single-level collection game built using Python and the Pygame library. Navigate the hero to collect all items while avoiding hazardous zones.

---

### 🕹️ How to Play
I kept the controls pretty standard so it's easy to pick up:
* **Move around:** Use the `Left` and `Right` arrow keys.
* **Jump:** Hit the `Spacebar` (I added gravity, so you'll fall back down!).
* **The Goal:** There are 5 gold coins scattered around. You win once you've touched all of them.
* **The Hazard:** Watch out for the red "Lava" in the middle of the floor. If you hit it, you'll get sent right back to the start!

---

### 🛠️ What I worked on (Bonus Features)

**1. The Lava (Death Zone)**
I wanted to add some stakes to the game, so I created a lava pit. I used a collision check so that whenever the player's hitbox overlaps with the lava's coordinates, the character's position resets to the beginning. It also prints a little "Ouch!" message in the console.

**2. Character Sprites & Flipping**
Instead of just moving a colored box around, I used a custom pixel-art sprite. 
* I used `blit` to draw the image onto the screen.
* I also added a bit of logic to check which way the player is moving. If you're moving left, I used `pygame.transform.flip` to mirror the sprite so she actually faces the direction she’s walking.

---

### 📦 Setup
To run this yourself, you'll just need:
* Python 3
* The Pygame library (`pip install pygame`)
* The `player.png` image file placed in the same folder as the script.
