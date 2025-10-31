# TypeScript Game Development Examples

These examples demonstrate how TypeScript's type system prevents common runtime errors in game development while making code more maintainable and self-documenting.

## Game Idea 1: Memory Card Matching Game

### The Problem (JavaScript)

```javascript
// Without TypeScript, it's easy to make mistakes with card state management
function createCard(value) {
  return {
    value: value,
    isFlipped: false,
    isMatched: false,
  };
}

// Easy to accidentally access undefined properties
function flipCard(card) {
  card.isFliped = true; // Typo! Should be isFlipped
  // No error in JavaScript, but game logic breaks
}

// Easy to pass wrong data types
let cards = [
  createCard("A"),
  createCard("A"),
  createCard(1), // Oops! Mixed types
  createCard("B"),
];
```

### The Solution (TypeScript)

```typescript
// Define interfaces for game objects
interface Card {
  id: number;
  value: string;
  isFlipped: boolean;
  isMatched: boolean;
}

interface GameState {
  cards: Card[];
  flippedCards: Card[];
  moves: number;
  matches: number;
  gameOver: boolean;
  startTime: Date;
}

// Type-safe card creation
function createCard(id: number, value: string): Card {
  return {
    id,
    value,
    isFlipped: false,
    isMatched: false,
  };
}

// Type-safe card flipping with proper property names
function flipCard(card: Card): void {
  if (!card.isMatched) {
    // Can only flip unmatched cards
    card.isFlipped = true; // TypeScript catches typos like "isFliped"
  }
}

// Type-safe game initialization
function initializeGame(cardValues: string[]): GameState {
  const cards: Card[] = [];
  let id = 0;

  // Create pairs of cards
  for (const value of cardValues) {
    cards.push(createCard(id++, value));
    cards.push(createCard(id++, value));
  }

  // Shuffle cards (Fisher-Yates algorithm)
  for (let i = cards.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [cards[i], cards[j]] = [cards[j], cards[i]];
  }

  return {
    cards,
    flippedCards: [],
    moves: 0,
    matches: 0,
    gameOver: false,
    startTime: new Date(),
  };
}

// Type-safe game logic
function handleCardClick(gameState: GameState, cardId: number): GameState {
  const card = gameState.cards.find((c) => c.id === cardId);

  // TypeScript ensures card exists before accessing properties
  if (!card || card.isFlipped || card.isMatched) {
    return gameState; // No change if card can't be flipped
  }

  // Flip the card
  flipCard(card);

  // Add to flipped cards
  const newFlippedCards = [...gameState.flippedCards, card];

  let newMatches = gameState.matches;
  let newGameOver = gameState.gameOver;

  // Check for match when two cards are flipped
  if (newFlippedCards.length === 2) {
    const [firstCard, secondCard] = newFlippedCards;

    if (firstCard.value === secondCard.value) {
      // Match found
      firstCard.isMatched = true;
      secondCard.isMatched = true;
      newMatches += 1;

      // Check if game is over
      if (newMatches === gameState.cards.length / 2) {
        newGameOver = true;
      }
    } else {
      // No match - flip cards back after delay
      setTimeout(() => {
        firstCard.isFlipped = false;
        secondCard.isFlipped = false;
      }, 1000);
    }

    // Reset flipped cards
    return {
      ...gameState,
      flippedCards: [],
      moves: gameState.moves + 1,
      matches: newMatches,
      gameOver: newGameOver,
    };
  }

  // Update flipped cards
  return {
    ...gameState,
    flippedCards: newFlippedCards,
    moves: gameState.moves + 1,
  };
}
```

## Game Idea 2: Space Shooter Game

### The Problem (JavaScript)

```javascript
// Without TypeScript, it's easy to have inconsistent object structures
function createPlayer() {
  return {
    x: 100,
    y: 100,
    // Missing properties that might be expected elsewhere
  };
}

function createEnemy() {
  return {
    x: 500,
    y: 50, // Oops! Should probably be a random position
    // Missing health, speed, etc.
  };
}

// Easy to make mistakes with collision detection
function checkCollision(obj1, obj2) {
  // What if obj1 or obj2 don't have x/y properties?
  return obj1.x === obj2.x && obj1.y === obj2.y; // Overly simplistic
}
```

### The Solution (TypeScript)

```typescript
// Define interfaces for game entities
interface Position {
  x: number;
  y: number;
}

interface Dimensions {
  width: number;
  height: number;
}

interface GameObject extends Position, Dimensions {
  id: number;
  velocity: { x: number; y: number };
}

interface Player extends GameObject {
  lives: number;
  score: number;
  isShooting: boolean;
}

interface Enemy extends GameObject {
  health: number;
  maxHealth: number;
  points: number;
  type: "basic" | "fast" | "tank";
}

interface Projectile extends GameObject {
  damage: number;
  isPlayerProjectile: boolean;
}

interface GameState {
  player: Player;
  enemies: Enemy[];
  projectiles: Projectile[];
  score: number;
  level: number;
  gameOver: boolean;
}

// Type-safe object creation
function createPlayer(): Player {
  return {
    id: 0,
    x: 400,
    y: 500,
    width: 50,
    height: 30,
    velocity: { x: 0, y: 0 },
    lives: 3,
    score: 0,
    isShooting: false,
  };
}

function createEnemy(
  type: "basic" | "fast" | "tank",
  x: number,
  y: number
): Enemy {
  const baseEnemy: Enemy = {
    id: Date.now(), // Simple ID generation
    x,
    y,
    width: 40,
    height: 40,
    velocity: { x: 0, y: 0 },
    health: 1,
    maxHealth: 1,
    points: 100,
    type,
  };

  // Customize based on type
  switch (type) {
    case "fast":
      baseEnemy.velocity.x = -2;
      baseEnemy.points = 150;
      break;
    case "tank":
      baseEnemy.health = 3;
      baseEnemy.maxHealth = 3;
      baseEnemy.points = 300;
      baseEnemy.width = 60;
      baseEnemy.height = 60;
      break;
    default: // basic
      baseEnemy.velocity.x = -1;
  }

  return baseEnemy;
}

// Type-safe collision detection
function checkCollision(obj1: GameObject, obj2: GameObject): boolean {
  return (
    obj1.x < obj2.x + obj2.width &&
    obj1.x + obj1.width > obj2.x &&
    obj1.y < obj2.y + obj2.height &&
    obj1.y + obj1.height > obj2.y
  );
}

// Type-safe game update logic
function updateGameState(currentState: GameState): GameState {
  // Update player position
  const updatedPlayer: Player = {
    ...currentState.player,
    x: currentState.player.x + currentState.player.velocity.x,
    y: currentState.player.y + currentState.player.velocity.y,
  };

  // Update enemy positions
  const updatedEnemies: Enemy[] = currentState.enemies
    .map((enemy) => ({
      ...enemy,
      x: enemy.x + enemy.velocity.x,
      y: enemy.y + enemy.velocity.y,
    }))
    .filter((enemy) => enemy.x > -100); // Remove off-screen enemies

  // Update projectile positions
  const updatedProjectiles: Projectile[] = currentState.projectiles
    .map((projectile) => ({
      ...projectile,
      x: projectile.x + projectile.velocity.x,
      y: projectile.y + projectile.velocity.y,
    }))
    .filter(
      (projectile) =>
        projectile.x > -50 &&
        projectile.x < 850 &&
        projectile.y > -50 &&
        projectile.y < 650
    ); // Remove off-screen projectiles

  // Check collisions between player projectiles and enemies
  const {
    enemies: remainingEnemies,
    projectiles: remainingProjectiles,
    scoreIncrease,
  } = checkProjectileEnemyCollisions(updatedEnemies, updatedProjectiles);

  // Check collisions between player and enemies
  const playerHit = checkPlayerEnemyCollisions(updatedPlayer, remainingEnemies);
  const finalPlayer = playerHit
    ? { ...updatedPlayer, lives: updatedPlayer.lives - 1 }
    : updatedPlayer;

  // Check game over condition
  const gameOver = finalPlayer.lives <= 0;

  return {
    ...currentState,
    player: finalPlayer,
    enemies: remainingEnemies,
    projectiles: remainingProjectiles,
    score: currentState.score + scoreIncrease,
    gameOver,
  };
}

function checkProjectileEnemyCollisions(
  enemies: Enemy[],
  projectiles: Projectile[]
): { enemies: Enemy[]; projectiles: Projectile[]; scoreIncrease: number } {
  let scoreIncrease = 0;
  let remainingEnemies = [...enemies];
  let remainingProjectiles = [...projectiles];

  // Check each projectile against each enemy
  for (let i = remainingProjectiles.length - 1; i >= 0; i--) {
    const projectile = remainingProjectiles[i];

    if (!projectile.isPlayerProjectile) continue; // Only player projectiles hit enemies

    for (let j = remainingEnemies.length - 1; j >= 0; j--) {
      const enemy = remainingEnemies[j];

      if (checkCollision(projectile, enemy)) {
        // Hit detected
        enemy.health -= projectile.damage;

        // Remove projectile
        remainingProjectiles.splice(i, 1);

        if (enemy.health <= 0) {
          // Enemy destroyed
          scoreIncrease += enemy.points;
          remainingEnemies.splice(j, 1);
        }

        break; // Projectile can only hit one enemy
      }
    }
  }

  return {
    enemies: remainingEnemies,
    projectiles: remainingProjectiles,
    scoreIncrease,
  };
}

function checkPlayerEnemyCollisions(player: Player, enemies: Enemy[]): boolean {
  for (const enemy of enemies) {
    if (checkCollision(player, enemy)) {
      return true;
    }
  }
  return false;
}
```

## Game Idea 3: Snake Game

### The Problem (JavaScript)

```javascript
// Without TypeScript, it's easy to have issues with snake segments
function createSnake() {
  return [
    { x: 10, y: 10 },
    { x: 9, y: 10 },
    { x: 8, y: 10 },
    // What if we accidentally add a segment without x/y?
  ];
}

// Easy to make mistakes with direction handling
function moveSnake(snake, direction) {
  const head = snake[0];

  // What if direction is invalid?
  switch (direction) {
    case "up":
      head.y -= 1;
      break;
    case "down":
      head.y += 1;
      break;
    // Missing left/right cases?
  }

  // What if we forget to add the new head or remove the tail?
}
```

### The Solution (TypeScript)

```typescript
// Define interfaces for snake game
interface Position {
  x: number;
  y: number;
}

interface SnakeSegment extends Position {}

type Direction = "up" | "down" | "left" | "right";

interface GameState {
  snake: SnakeSegment[];
  food: Position;
  direction: Direction;
  nextDirection: Direction;
  score: number;
  gameOver: boolean;
  gridWidth: number;
  gridHeight: number;
}

// Type-safe snake creation
function createInitialSnake(): SnakeSegment[] {
  return [
    { x: 10, y: 10 }, // Head
    { x: 9, y: 10 }, // Body
    { x: 8, y: 10 }, // Tail
  ];
}

// Type-safe food generation
function generateFood(
  snake: SnakeSegment[],
  gridWidth: number,
  gridHeight: number
): Position {
  let food: Position;
  let foodOnSnake: boolean;

  do {
    food = {
      x: Math.floor(Math.random() * gridWidth),
      y: Math.floor(Math.random() * gridHeight),
    };

    // Check if food is on snake
    foodOnSnake = snake.some(
      (segment) => segment.x === food.x && segment.y === food.y
    );
  } while (foodOnSnake);

  return food;
}

// Type-safe direction handling
function changeDirection(
  currentDirection: Direction,
  newDirection: Direction
): Direction {
  // Prevent 180-degree turns
  if (
    (currentDirection === "up" && newDirection === "down") ||
    (currentDirection === "down" && newDirection === "up") ||
    (currentDirection === "left" && newDirection === "right") ||
    (currentDirection === "right" && newDirection === "left")
  ) {
    return currentDirection; // Keep current direction
  }

  return newDirection;
}

// Type-safe snake movement
function moveSnake(
  snake: SnakeSegment[],
  direction: Direction,
  food: Position
): { newSnake: SnakeSegment[]; ateFood: boolean } {
  // Create new head based on direction
  const head = snake[0];
  let newHead: SnakeSegment;

  switch (direction) {
    case "up":
      newHead = { x: head.x, y: head.y - 1 };
      break;
    case "down":
      newHead = { x: head.x, y: head.y + 1 };
      break;
    case "left":
      newHead = { x: head.x - 1, y: head.y };
      break;
    case "right":
      newHead = { x: head.x + 1, y: head.y };
      break;
  }

  const newSnake = [newHead, ...snake];
  let ateFood = newHead.x === food.x && newHead.y === food.y;

  // If snake didn't eat food, remove tail
  if (!ateFood) {
    newSnake.pop();
  }

  return { newSnake, ateFood };
}

// Type-safe collision detection
function checkCollisions(
  snake: SnakeSegment[],
  gridWidth: number,
  gridHeight: number
): boolean {
  const head = snake[0];

  // Check wall collision
  if (head.x < 0 || head.x >= gridWidth || head.y < 0 || head.y >= gridHeight) {
    return true;
  }

  // Check self collision (skip head)
  for (let i = 1; i < snake.length; i++) {
    if (head.x === snake[i].x && head.y === snake[i].y) {
      return true;
    }
  }

  return false;
}

// Type-safe game update
function updateGameState(currentState: GameState): GameState {
  // Update direction
  const updatedDirection = changeDirection(
    currentState.direction,
    currentState.nextDirection
  );

  // Move snake
  const { newSnake, ateFood } = moveSnake(
    currentState.snake,
    updatedDirection,
    currentState.food
  );

  // Check for collisions
  const collisionDetected = checkCollisions(
    newSnake,
    currentState.gridWidth,
    currentState.gridHeight
  );

  if (collisionDetected) {
    return {
      ...currentState,
      gameOver: true,
    };
  }

  // Generate new food if snake ate the current one
  const newFood = ateFood
    ? generateFood(newSnake, currentState.gridWidth, currentState.gridHeight)
    : currentState.food;

  // Update score
  const newScore = ateFood ? currentState.score + 10 : currentState.score;

  return {
    ...currentState,
    snake: newSnake,
    food: newFood,
    direction: updatedDirection,
    score: newScore,
  };
}
```

## Benefits of Using TypeScript for Game Development

1. **Object Structure Consistency**: Interfaces ensure all game objects have the required properties
2. **Error Prevention**: Type checking catches mistakes at compile time rather than runtime
3. **Refactoring Safety**: When changing object structures, TypeScript shows exactly what needs to be updated
4. **Code Documentation**: Type annotations serve as documentation for team members
5. **IntelliSense Support**: Better autocomplete and development experience in IDEs
6. **State Management**: Union types help manage different game states safely

These game examples demonstrate how TypeScript's type system prevents common errors in game development while making the code more maintainable and self-documenting.
