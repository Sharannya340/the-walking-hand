## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`ODT-2026-The Walikng Hand`

NEW- 
`ODT-2026-TEAM PULSE`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `[Sharannya Sakorkar]` | `[Mechanics]` | `[Fabrication + Electronics]` | `[Mechanics]` |
| `[Aayushi Shirodkar]` | `[Coding]` | `[Fabrication + Electronics]` | `[Coding]` |

NEW- 
| `[Sharannya Sakorkar]` | `[Mechanics]` | `[Fabrication + Electronics]` | `[Hands-on building, assembly]` |
| `[Aayushi Shirodkar]` | `[Coding]` | `[Fabrication + Electronics]` | `[Logic building]` |


## 1.3 Project Title
`[The Walking Hand]`

NEW- 
`[PULSE]`

## 1.4 One-Line Pitch
`[Netflix's Wednesday-inspired, switch-operated, creepy walking hand, that pranks users.]`

NEW- 
`[A rhythm-based interactive game where players follow on-screen prompts and respond using a physical hand interface.]`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`[The Walking Hand is a Wednesday-series inspired project, built to human scale- a 3D-printed skeletal hand that walks on its own, with no body attached and no explanation offered. At the press of a switch, its fingers come alive: some wiggle, some walk, and the whole thing moves with just enough personality to prank you in the best possible way.
What powers it is best left mostly to the imagination- but underneath the glove, there is circuitry, there are motors, and there is a microcontroller quietly doing its job. The result is something that sits right at the intersection of engineering and eeriness, equal parts curious artefact and crowd-stopper.]`

NEW- 
`[Pulse is an interactive musical game built using Pygame and a physical hand-shaped controller. The system plays a song and displays visual prompts indicating which finger the player must press. The player responds by tapping the corresponding finger on a red hand skeleton model connected to an ESP32. The experience is fast-paced and reflex-driven. Players must react quickly and accurately to score points. The system provides real-time feedback such as “Perfect,” “Good,” or “Miss,” based on timing and accuracy. Each round lasts 40 seconds, making it engaging, repeatable, and competitive.]`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`[The Walking Hand is a fun, interactive experience, that first pranks the audience, then fascinates them, and lastly, sparks curiosity in them. It puts a single switch in front of you and dares you to press it. When you do, a gloved, skeletal hand springs to life- fingers wiggling, walking, and moving with a mechanical confidence that feels both exciting and confusing. The experience is meant to be immediate, tactile, and impossible to look away from. The experience is designed to be familiar enough to unsettle, strange enough to fascinate. We want people to return- return with questions- How does it work? Can it go faster? What happens if I press it again? That loop of wonder and curiosity is the real mechanism at play.]`

NEW- 
`[This is a fast-paced, reflex-based musical interaction. The player feels alert, engaged, and slightly challenged. The quick feedback and scoring system make the experience addictive and encourage repeated play.]`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`[We are designing this project as if we are a small creative studio making an interactive experience for people of all age groups to enjoy.]`

NEW- 
`[We are designing this project as if we are a small creative studio making a playable interactive game for teens, classmates, and exhibition visitors.]`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `[Netflix series- Wednesday]` | `[Thing]` | `[We were initally going to make a walking foot, but the series' Thing inspired us to switch to making a walking hand.]` |
| `[Biomechanics]` | `[Human Hand Anatomy & Tendon-Drive Mechanisms]` | `[We understood how fingers flex, curl, and bear weight through pivot joints, which helped shape our 3D-printed skeletal structure and motor placement]` |
| `[Prosthetic Limb Research` | `[Luke Arm]` | `[Study on anatomical framework for how motors map to realistic finger movement]` |

NEW-
| `[Game]` | `[Reflex action games (general)]` | `[Following instruction and reacting in time]` |
| `[App]` | `[Piano Tiles]` | `[Fast tapping interaction]` |
| `[Object]` | `[Keyboard]` | `[Finger-based input system]` |


## 3.2 Original Twist
What makes your project original?

**Response:**  
`[It is a fun, harmless prank menat to spread laughter and excitement.]`

NEW-
`[The use of a physical hand-shaped controller instead of a keyboard creates a more fun, engaging and tactile experience.]`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`[press → activate → walk & wiggle → release → reset
The participant presses the switch, which pulls GPIO 14 LOW and triggers the main loop. Instantly and simultaneously, the DC motors drive the index and little fingers forward in a walking motion, while the servo motors step through a sequence of angles — 30°, 90°, 150°, 90° — cycling every 0.3 seconds to produce a continuous, rhythmic wiggle in the middle and ring fingers. The hand walks for as long as the switch is held. The moment it is released, all four motors stop, both servos return to their neutral 90° position, and the wiggle counter resets to zero, leaving the hand exactly as it was found, ready for the next press.]`

NEW-
`[read instructions → be alert → see prompt → identify finger → tap finger → system checks → feedback → repeat → score]`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `[People of all age groups]` |
| Age range | `[Approximately 10-70]` |
| Solo or multiplayer | `[Solo]` |
| Expected duration of one round | `[5 minutes]` |
| What should the player feel? | `[surprise, excitement, curiosity]` |
| Is explanation required before use? | `[This is a switch-operated hand. There is one control and one instruction: press the button, and the hand walks. Release it, and it stops. No setup is required, no prior knowledge is needed, and nothing about it is complicated. Press it, watch it, and try not to look away.]` |

NEW-
| Who is this for? | `[People of all age groups]` |
| Age range | `[Approximately 12+]` |
| Solo or multiplayer | `[Solo]` |
| Expected duration of one round | `[40 seconds]` |
| What should the player feel? | `[engaged, challenged, excited]` |
| Is explanation required before use? | `[Minimal instructions]` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[The player is interacting with a website.]`
2. **Start:** `[They read the one-line instruction- press the switch, and do exactly that.]`
3. **First Action:** `[Suddenly, the hand comes out of nowhere and pranks the user.]`
4. **Main Interaction:** `[They hold the button down and watch the hand respond, keeping it pressed for as long as they want to see it move.]`
5. **System Response:** `[The moment the button is pressed, all four motors activate simultaneously. The index and little fingers begin walking the hand forward across the surface, while the middle and ring fingers wiggle in a rhythmic, repeating sequence.]`
6. **Win / Lose / End Condition:** `[ There is no win or lose condition. The interaction ends when the player releases the button- the motors stop, the fingers return to their resting position, and the hand goes still.]`
7. **Reset:** `[The hand is ready for the next press without any manual intervention.]`

NEW-
1. **Approach:** `[The player sees the setup with the hand and screen]`
2. **Start:** `[Game begins with starting instrcutions and music]`
3. **First Action:** `[Player observes first prompt- any finger, then the next, and so on]`
4. **Main Interaction:** `[Player taps correct fingers continuously]`
5. **System Response:** `[Displays “Perfect”, “Good”, or “Miss”, according to the response time]`
6. **Win / Lose / End Condition:** `[ There is no win or lose condition. The player gets their score in the endGame ends after 40 seconds. ]`
7. **Reset:** `[Game restarts for next player.]`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `[Not Applicable, since this is not a game.]`

NEW-
- `[Follow the on-screen finger prompts
Tap the correct finger on the hand model
Faster and accurate responses score higher
Game ends after 40 seconds]`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `[The system activates upon switch input and responds without perceptible delay]`
- [ ] `[All four fingers execute their intended motions]`
- [ ] `[The hand demonstrates stable, controlled forward movement without collapsing or losing balance]`
- [ ] `[The hand resets to its neutral state immediately upon release of the switch]`
- [ ] `[At least 3 out of 5 test users express clear engagement (surprise, curiosity, or fascination) during interaction]`

NEW-
- [ ] `[System runs without crashing]`
- [ ] `[Inputs are detected correctly]`
- [ ] `[Feedback is displayed accurately]`
- [ ] `[Game completes full 40-second cycle]`
- [ ] `[Player understands how to play]`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`[The minimum viable version consists of a structurally stable hand capable of executing a single, clear motion in response to input. This includes one working finger driven by a motor or servo and a functional switch input. While full walking motion and multi-finger coordination may be absent, the core experience, pressing a button and witnessing an inanimate hand come to life, must remain intact. The emphasis at this stage is not complexity, but credibility of responsiveness.]`

NEW-
`[A working version where different keys on the keyboard are used to play, matched with on-screen prompts, with basic scoring and feedback.]`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `[Variable speed control allowing users to modulate the pace of movement.]`
- `[Improved gait mechanics enabling smoother, more lifelike walking across different surfaces.]`
- `[The appearance of a real, life-like hand instead of a model.]`

NEW-
- `[Choice of songs]`
- `[Difficulty levels- Easy, Medium, Hard]`
- `[Enhanced visuals]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [✅] Electronics-based
- [✅] Mechanical
- [ ] Sensor-based
- [ ] App-connected
- [✅] Motorized
- [ ] Sound-based
- [ ] Light-based
- [ ] Screen/UI-based
- [✅] Fabricated structure
- [ ] Game logic based
- [ ] Installation / tabletop experience
- [✅] Other: `[Prank/experience/reaction based]`

NEW-
- [✅] Electronics-based
- [ ] Mechanical
- [✅] Sensor-based
- [ ] App-connected
- [ ] Motorized
- [✅] Sound-based
- [ ] Light-based
- [✅] Screen/UI-based
- [ ] Fabricated structure
- [✅] Game logic based
- [✅] Installation / tabletop experience
- [✅] Other: `[Reflex action/ reaction based]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`[The system operates as a closed-loop interactive mechanism translating a simple human input into coordinated mechanical motion. The primary input is a physical switch, which, when pressed, sends a signal to the ESP32 microcontroller. The controller processes this input and executes a predefined control logic that simultaneously drives DC motors and servo motors. The DC motors generate forward locomotion by actuating specific fingers, while the servo motors articulate the remaining fingers through controlled angular movement. All components are embedded within a fabricated skeletal hand structure, which houses the wiring, motors, and joints. There is no app-based interaction; the system is intentionally self-contained to preserve immediacy and tactile engagement. The output is purely physical: motion, rhythm, and presence.]`

NEW-
`[The player taps fingers on a physical hand model. Each finger is connected to the ESP32, which sends input signals to the computer. The Pygame program processes the input and compares it with the expected prompt. Based on accuracy and timing, the system displays feedback and updates the score.]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[Switch]` | Input | `[Captures user intent; when pressed, sends a LOW signal to initiate the motion sequence.]` |
| `[ESP32]` | Processing | `[Interprets input signal and executes programmed logic to coordinate motor and servo activity.]` |
| `[Servos + DC Motors]` | Output | `[DC motors drive forward locomotion; servo motors control wiggling motion in the fingers.]` |
| `[3D-Printed Hand Skeleton]` | Physical Action | `[Translates motor output into visible, tactile movement through its structure.]` |

NEW-
| `[Finger inputs]` | Input | `[Detects players taps]` |
| `[ESP32]` | Processing | `[Interprets input signal and sends signals to system]` |
| `[Pygame]` | Processing | `[Matches input with prompts]` |
| `[Laptop screen]` | Output | `[Displays prompts, feedback and final score]` |
| `[Hand model]` | Physical action | `[Interactive physical interface for player]` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[20 cm]` |
| Width | `[15.2 cm]` |
| Height | `[28.4 cm]` |
| Estimated weight | `[approximately 50 gm]` |

NEW-
| Length | `[20 cm]` |
| Width | `[15.2 cm]` |
| Height | `[13.5 cm]` |
| Estimated weight | `[approximately 50 gm]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [✅] Linkages
- [✅] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [ ] Not applicable

NEW-
`[Not applicable to our new project.]`

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[The mechanical system is designed to replicate simplified hand biomechanics through a combination of rigid structures and articulated joints. Each finger is constructed as a segmented linkage system, connected via hinge-like joints that allow controlled bending. Motion is driven through motor-actuated pull mechanisms, where rotational motion is translated into linear tension, simulating tendon-like behavior. Select fingers are optimized for load-bearing and propulsion, enabling the hand to shift its weight and move forward, while others are tuned for expressive articulation. The mechanism prioritizes clarity of motion over anatomical precision, ensuring that each movement is both mechanically feasible and visually legible.]`

NEW-
`[The project does not involve moving mechanical parts. The hand model is static and used as an input interface.]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[The index and little fingers are responsible for forward locomotion that propels the hand across a flat surface. This movement is driven by DC motors, converting rotational energy into incremental shifts in position. The middle and ring fingers are actuated by servo motors, cycling through predefined angular positions to produce a continuous wiggling effect. Each motion cycle spans approximately 0.3 seconds, creating a rhythmic and synchronized output. The range of motion is deliberately constrained to maintain structural stability and prevent overextension. Potential failure points include imbalance leading to tipping, insufficient friction causing slippage, misalignment of joints affecting smooth motion, and motor torque limitations under load.]`

NEW-
`[Not applicable to the new project.]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Blender]` | `[Link or screenshot]` | `[Scale, shape, hinges and joints]` |

NEW-
`[Same as before.]`


## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[After test printing our initial model, we realised it was too small. So we scaled it up and made it the size of a human hand.]`

NEW-
`[Same as before.]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `[Servo Motor]` | `[2]` | `[Wiggling in two fingers]` |
| `[DC Motor]` | `[2]` | `[Forward motion in the hand]` |
| `[Switch]` | `[1]` | `[Starting the motion in the hand]` |
| `[Power Supply]` | `[1]` | `[Supplying power to the circuit]` |

NEW-
| `[ESP32]` | `1` | `[Main controller]` |
| `[Wires]` | `[Multiple]` | `[Connections]` |
| `[Breadboard]` | `[1]` | `[Circuit setup]` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[The ESP32 is the main controller. The switch is connected to the ESP32 to start the whole motion. All 4 motors draw their power from the external power supply, not the ESP32.]`

NEW-
`[Each finger of the hand model is connected to the ESP32 using wires. When a finger is tapped, it sends a signal to the ESP32, which communicates it to the system on the laptop.]`


## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[USB / battery / adapter / other]` |
| Voltage required | `[5V for servos and logic, with regulated supply as needed]` |
| Current concerns | `[Motor startup current and simultaneous load may cause voltage drops; requires stable supply or driver support]` |
| Safety concerns | `[Avoid overheating, ensure proper insulation of connections, and prevent short circuits during operation]` |

NEW-
| Power source | `[ESP32]` |
| Voltage required | `[3.3V ]` |
| Current concerns | `[Stable connection required]` |
| Safety concerns | `[Avoid short circuits]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython]` | `[Serves as the core programming environment that translates user input into coordinated motor and servo actions.]` |
| `[Thonny]` | `[It is used as the primary tool to develop, test, and deploy the control logic onto the ESP32 efficiently.]` |

NEW-
| `[MicroPython (Thonny)]` | `[Hardware control]` |
| `[Pygame]` | `[Game interface]` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[On starting, the system sets servo motors to their neutral position, and ensures DC motors are in an off state. The program then enters a continuous loop, monitoring the switch input. When the switch is pressed, the controller executes a synchronized routine: DC motors are activated to initiate forward motion, while servo motors cycle through predefined angular values to generate a rhythmic wiggle. This loop continues for as long as the input remains active. Upon release, the system immediately halts all motor activity, returns servos to neutral, and resets internal counters. The logic is intentionally minimal, prioritizing responsiveness and repeatability over complexity.]`

NEW-
`[The program starts by initializing the game and playing music. It displays prompts indicating which finger to press. The system continuously checks for input from the ESP32. Based on timing and correctness, it displays feedback and updates the score. After 40 seconds, the game ends and shows the final score.]`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Image uploaded]`

## 10.4 Pseudocode

```text
[# include the servo library
# include the time library
# include the pin library
# ── SWITCH ─────────────────────────────────────────────────
# initialise the switch pin as an input with pull-down
# ── SERVO SETUP ────────────────────────────────────────────
# initialise the pins to be outputs - Servo is an output device
# middle finger
# ring finger
# initialise the servos for use
# ── DC MOTOR SETUP ─────────────────────────────────────────
# initialise the DC motor pins as outputs
# index finger - forward
# index finger - keep LOW
# little finger - forward
# little finger - keep LOW
# ── WIGGLE ANGLES ──────────────────────────────────────────
# the servo will step between these angles to wiggle the finger
# ── MOTOR CONTROL FUNCTIONS ────────────────────────────────
# turn both DC motors on (index and little finger move forward)
# turn both DC motors off
# stop both servos (write to neutral and release)
# ── MAIN LOOP ──────────────────────────────────────────────
# switch is PRESSED
        # DC motors run continuously while switch is held
        # servos wiggle through the angle list one step at a time
        # move to next angle in the wiggle sequence
        # small delay between each wiggle step
# switch is NOT pressed
# reset wiggle for next press
# small idle delay]

NEW-
`[#Touch pins
# Map: key → (TouchPad, keycode, modifier)
# Simple debounce tracking
# Touch detected]`

pygame code:
`[# ───────── CONFIG ─────────
# ───────── INIT ─────────
# ───────── VISUALS ─────────
# ───────── GAME STATE ─────────
# ───────── MAIN LOOP ─────────
# ───────── DRAW ─────────
# AUTO MISS]`



```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [✅] No

NEW-
`[Same as before.]`

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `Yes` | `284` | `[Microcontroller]` | `[The one in the kit stopped working]` |
| `[Power supply (buck converter)]` | `[1]` | `[No]` | `[Yes]` | `[50]` | `[Spec]` | `[Backup, incase the power supply stopped working because of 4 motors]` |
| `[Car]` | `[1]` | `[No]` | `[Yes]` | `[399]` | `[Material]` | `[We needed the DC motors from the toy car]` |
| `[Servo motor]` | `1` | `Yes` | `Yes` | `140` | `[Spec]` | `[Servos in the kit stopped working]` |

NEW-
| `[ESP32]` | `1` | `Yes` | `Yes` | `284` | `[Microcontroller]` | `[The one in the kit stopped working]` |
| `[Wires]` | `Multiple` | `Yes` | `No` | `0` | `[Copper]` | `[Connections]` |
| `[Breadboard]` | `1` | `Yes` | `No` | `0` | `[Plastic]` | `[Easy setup]` |
| `[MDF board]` | `1` | `No` | `No` | `0` | `[Wood]` | `[Stable base]` |
| `[3D Printed Hand]` | `1` | `No` | `No` | `0` | `[PLA]` | `[Interactive element]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Materials and components were selected to balance precision, feasibility, and structural reliability. 3D printing was chosen for the hand structure due to its ability to produce complex geometries and jointed forms with high accuracy, which would be difficult to achieve using manual fabrication methods. Servo motors were used for finger articulation because of their precise angle control, while DC motors were selected for locomotion due to their continuous rotational capability and higher torque output. Lightweight materials were prioritized to reduce load on the motors, improving efficiency and stability. Overall, each choice reflects a trade-off between performance, accessibility, and ease of iteration within the given timeframe.]`

NEW-
`[MDF provides a stable base. The 3D printed hand allows accurate finger placement and a fun interactive experience. ESP32 is used for easy input handling.]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[ESP32]` | `[Our original ESP32 got fried]` | `[Link]` | `[7th April]` | `[Received]` |
| `[2 DC MOTORS]` | `[Our original DC motors were uresponsive]` | `[Link]` | `[7th April]` | `[Received]` |
| `[2 SERVO MOTORS]` | `[Our original servo motors were uresponsive]` | `[Link]` | `[7th April]` | `[Received]` |
| `[POWER SUPPLY]` | `[Backup incase of overload]` | `[Link]` | `[14th April]` | `[Received]` |
| `[TISSUE PAPER]` | `[Paper mache outer covering]` | `[Link]` | `[15th april]` | `[Received]` |

NEW-
 `[Nothing separately for the new project.]`


## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[873]` |
| Mechanical parts | `[Cost]` |
| Fabrication materials | `[332]` |
| Purchased extras | `[Cost]` |
| Contingency | `[Cost]` |
| **Total** | `[1205]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[NA]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`[Technical decisions are made through discussions, prioritizing feasibility within the time constraints. Progress is reviewed at regular intervals. Documentation is a continuous process, done to capture iterations, stages of the project, challenges and how we overcome them.]`

NEW-
`[Even though we had to change our concept last minute due to unforseen obstacles, we managed it. We took turns making decisions, stayed and worked together despite the hopelessness and pulled through in the end.]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Aayushi and Sharannya]` | `2` | `[7th april]` | `None` | `Done` |
| T2 | `[Complete BOM]` | `[Aayushi]` | `1` | `[19th april]` | `T1` | `To Do` |
| T3 | `[Test electronics]` | `[Aayushi and Sharannya]` | `3` | `[14th april]` | `T1` | `Done` |
| T4 | `[Build structure]` | `[Sharannya]` | `4` | `[15th april]` | `T1` | `Ongoing` |
| T5 | `[Write control code]` | `[Aayushi]` | `4` | `[14th april]` | `T3` | `Done` |
| T6 | `[Integrate system]` | `[Sharannya]` | `4` | `[18th april]` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `[Sharannya]` | `2` | `[20th april]` | `T6` | `Ongoing` |
| T8 | `[Refine and document]` | `[Aayushi]` | `4` | `[20th april]` | `T7` | `Ongoing` |

NEW-
| T1 | `[Finalize concept]` | `[Aayushi and Sharannya]` | `2` | `[20th april]` | `None` | `Done` |
| T2 | `[Complete BOM]` | `[Aayushi]` | `1` | `[20th april]` | `T1` | `Done` |
| T3 | `[Test electronics]` | `[Aayushi and Sharannya]` | `3` | `[20th april]` | `T1` | `Done` |
| T4 | `[Build structure]` | `[Sharannya]` | `4` | `[20th april]` | `T1` | `Done` |
| T5 | `[Write control code]` | `[Aayushi]` | `4` | `[20th april]` | `T3` | `Done` |
| T6 | `[Integrate system]` | `[Sharannya]` | `4` | `[20th april]` | `T4, T5` | `Done` |
| T7 | `[Playtest]` | `[Sharannya]` | `2` | `[20th april]` | `T6` | `Done` |
| T8 | `[Refine and document]` | `[Aayushi]` | `4` | `[20th april]` | `T7` | `Done` |


## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Sharannya]` | `[Aayushi]` |
| Electronics | `[Aayushi]` | `[Sharannya]` |
| Coding | `[Aayushi]` | `[Sharannya]` |
| App | `[NA]` | `[NA]` |
| Mechanical build | `[Sharannya]` | `[Aayushi]` |
| Testing | `[Sharannya]` | `[Aayushi]` |
| Documentation | `[Aayushi]` | `[Sharannya]` |

NEW-
`[Same as before.]`

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [✅] Idea finalized
- [ ] Core interaction decided
- [✅] Sketches made
- [ ] BOM completed
- [✅] Purchase needs identified
- [✅] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [✅] CAD / structure planning completed
- [ ] App UI started if needed
- [✅] Mechanical concept tested
- [✅] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [✅] Physical body built
- [✅] Electronics integrated
- [✅] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [✅] Technical bugs reduced
- [ ] Playtesting completed
- [✅] Improvements made
- [✅] Documentation completed
- [✅] Final build ready

NEW-
`[We had to scrap our inital idea of the prank on the night of 20th April because our H-Bridge and DC motors got fried. Hence, we came up with an entirely new concept and executed it in less than 24 hours.]`

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Concept finalisation and execution planning]` | `[Finalising our idea, getting to approved, and brainstorming its execution]` | `[We had initially planeed a walking foot or walking shoe, but upon more discussion, we committed to a walking hand]` | `[We had multiple meetings and researched on how to execute it]` |
| Week 2 | `[Source all the materials]` | `[Getting everything ready for building]` | `[Nothing]` | `[3d Printing and making the connections]` |
| Week 3 | `[Building]` | `[3d Printing, attaching the electronics, making the connections, adjusting the code]` | `[Our idea for the outer covering]` | `[Paper mache and prank planning]` |
| Week 4 | `[Refine and Finish]` | `[Working on its presentation for the final day]` | `[Ideas for final day prank]` | `[Prep for the exhibition]` |

NEW-
`[We had to scrap our inital idea of the prank on the night of 20th April because our H-Bridge and DC motors got fried. Hence, we came up with an entirely new concept and executed it in less than 24 hours.]`

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Motor torque insufficient for forward movement]` | `[Technical]` | `[Medium]` | `[High]` | `[Test under load early; reduce weight]` | `[Aayushi]` |
| `[Unstable gait causing tipping]` | `[Mechanical]` | `[Medium]` | `[High]` | `[Adjust center of gravity, redistribute weight]` | `[Sharannya]` |

NEW-
| `[Input not detected]` | `[Technical]` | `[Medium]` | `[High]` | `[Check Wiring]` | `[Team]` |
| `[Damage of parts]` | `[Material]` | `[Medium]` | `[High]` | `[Careful handling; taking extra precaution and not letting the ESP32 heat up]` | `[Team]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[The primary uncertainty lies in achieving stable locomotion again and again. While individual components—motors, servos, and joints—function as intended in isolation, their synchronized behavior after the outer visual elements are attached onto the skeleton remains an unresolved variable.]`

NEW-
`[Ensuring accurate and fast communication between hardware input and game response.]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Switch input reliability]` | `[Repeated manual press cycles under varying speeds and for varying time periods]` | `[Consistent and immediate response without false triggers]` |
| `[Mechanism movement]` | `[Running motion cycles for varying durations]` | `[Smooth, uninterrupted movement without mechanical failure]` |
| `[Servo motors]` | `[Observe synchronized angle transitions across cycles]` | `[Accurate, repeatable wiggling without jitters]` |
| `[DC motors]` | `[Test on different surfaces]` | `[Sustained forward movement without stalling]` |

NEW-
| `[Successful input]` | `[Manual testing]` | `[Correct detection of inputs]` |
| `[Game response]` | `[Running the program]` | `[Immediate feedback]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Observe if users press the switch without hesitation upon instruction]` |
| Is the interaction satisfying? | `[Record immediate reactions (facial expressions, see if they get successfully pranked or not)]` |
| Do players want another turn? | `[Track repeat interactions and voluntary re-engagement]` |
| Is the challenge balanced? | `[Not applicable]` |
| Is the response clear and immediate? | `[Measure delay between input and motion; observe user perception]` |

NEW-
| Do players understand what to do? | `[Observe if users handle the hand shaped mouse confidently after instrustion.]` |
| Is the interaction satisfying? | `[Record their game (facial expressions, see if they are getting challenged, having fun, getting stressed out)]` |
| Do players want another turn? | `[Track repeat interactions and voluntary re-engagement]` |
| Is the challenge balanced? | `[User feedback]` |
| Is the response clear and immediate? | `[Measure delay between input and response; observe user perception]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[15th April]` | `[Motion of the hand was sudden and jittery; Hand lost balance]` | `[Mechanical]` | `[Changed the position of the servos and DC motors and tested various combinations]` | `[Worked]` | `[Observing such probelms in the future]` |

NEW-
| `[20th april]` | `[H-bridge and DC motors got fried]` | `[Connections + Motion]` | `[Changed our project idea]` | `[Executed it]` | `[A new, successful project]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Radhika / friend / classmate]` | `[Follwed all the steps]` | `[Nothing]` | `[The movement]` | `[Increase the surprise element]` |

NEW-
| `[friend]` | `[Played the game]` | `[The immediate response that was required]` | `[The whole experience]` | `[Explanation of the instructions]` |
| `[classmate]` | `[Did everything calmly]` | `[The fast pace of the game]` | `[The game]` | `[Prepare players for the level of speed required.]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[The project was created through a structured sequence of digital modeling and physical assembly. The hand structure was first designed in Blender and 3D printed to achieve precision. Individual components were then cleaned, sanded, and fit. Motors and servos were mounted within the structure using mechanical fasteners and adhesives, with careful attention to alignment and load distribution. Wiring was routed internally to maintain a clean external form while ensuring accessibility for debugging. Iterative revisions were made throughout assembly, particularly in joint tolerances and motor placement, to improve stability and motion quality.]`

NEW-
`[The hand model was 3D printed and mounted on an MDF board, that was painted black. Wires were connected from each finger to the ESP32 through a breadboard. The system was tested multiple times and adjusted for stable input.]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[13th April]` | `[Basic structure with single motor movement]` | `[Validation of core motion feasibility]` |
| `v2` | `[14th April]` | `[Integrated all 4 motors and tested their simultaneous movement]` | `[Test interaction complexity]` |
| `v3` | `[16th April]` | `[Refined gait and balance]` | `[Perfect the motion]` |

NEW-
| `v1` | `[20th April]` | `[Walking hand with functioning motors]` | `[H-bridge and DC motors got fried]` |
| `v2` | `[20th April]` | `[Basic structure of new idea]` | `[Could not continue the old idea without those parts]`
| `v3` | `[21st April]` | `[Reflex action test game]` | `[Successful execution of new concept]` |


---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[The final outcome is a cool, motorized hand prank that responds instantly to user input, translating a simple press into coordinated, lifelike motion. The system successfully integrates mechanical design, electronics, and control into a cohesive interactive artefact. It achieves its intended effect—an object that is at once familiar and unsettling—by prioritizing clarity of motion, responsiveness, and physical presence over complexity.]`

NEW-
`[Pulse is a working interactive reflex action test + game that combines a digital interface with a physical input system. Players respond to on-screen prompts using a hand-shaped controller, receiving real-time feedback and a final score.]`

## 18.2 What Works Well
- `[Immediate and reliable input-to-motion response]`
- `[Clear, synchronized coordination between motors and servos]`
- `[Strong user engagement driven by novelty and uncanny motion]`

NEW-
- `[Clear interaction]`
- `[Responsive system]`
- `[Engaging gameplay]`

## 18.3 What Still Needs Improvement
- `[The visual, appearance]`
- `[Element of surprise]`
- `[More refined balance and weight distribution]`

NEW-
- `[A more visually poilshed and attractive project]`


## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[The project evolved from a simpler concept of finger movement to a cooler vision of a walking hand prank, incorporating a fun aesthetic and element of surprise. This shift required greater emphasis on mechanical stability, synchronization, aesthetics and load management. As a result, the design became less about individual motion fidelity and more about achieving a cohesive, believable system of movement.]`

NEW-
`[The original motor-based concept was replaced due to hardware failure, leading to a simpler and more reliable interaction system that is both a test and a game.]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Our team demonstrated strong alignment in vision, execution and consistent communication throughout the process. Progress was most effective when tasks were discussed, brainstormed and parallelized, particularly during early development stages. Delays primarily arose during integration, where interdependencies between mechanical and electronic systems required iterative troubleshooting. Overall, time and responsibilities were managed effectively, with adaptability playing a key role in maintaining momentum.]`

NEW-
`[The team collaborated effectively, adapted quickly to challenges and overcame obstacles. Time management improved over the project duration. We demonstrated unity in times of adversity and pulled through with constant communication. Overall, time and responsibilities were managed effectively.]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[This project deepened our understanding of how systems, electronics, code, and mechanics, interact under real-world constraints. We learned that reliable hardware behavior depends as much on power stability and physical alignment as it does on correct code. The integration phase revealed the importance of iterative testing, where small misalignments or inefficiencies compound into larger system-level issues. Most critically, we learned to design with constraints in mind rather than attempting to resolve them later.]`

NEW-
`[We learned about hardware-software integration, input handling, and debugging.]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[We learned that designing for play does not require complexity, but clarity and immediacy. The most effective interactions are those that communicate their function intuitively and respond without delay. The project reinforced the value of restraint- by limiting inputs and removing unnecessary layers, the experience became more focused and impactful. Iteration proved essential in refining, not just functionality, but the emotional response elicited by the object.]`


NEW-
`[We learned the importance of simplicity, clarity, and user interaction in design. We learned hwo to deal with adversity and last minute mishaps, and how to overcome them.]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Improvising the user experience, and creating an even cooler prank stages and atmosphere.]`

NEW-
`[We would have integrated more elements like neopixels or buzzers as part of the experience. We would have added levels to the game, like easy, medium and hard. We would have integrated a variety of songs for the players to choos from. We would have added more complexity and improved the presentation of the entire project.]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
