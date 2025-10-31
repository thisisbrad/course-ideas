# Real-World Simulation Activities

## "Legacy Code Rescue" Missions

### Mission 1: "The Untyped Shopping Cart"

**Scenario**: You've inherited a JavaScript shopping cart module riddled with type-related bugs
**Objective**: Incrementally add TypeScript types to eliminate runtime errors
**Buggy Code Issues**:

- Adding strings to number totals
- Undefined property access on cart items
- Incorrect discount calculations
- Inconsistent item structures

**Rescue Steps**:

1. Analyze existing JavaScript code for potential type errors
2. Add basic type annotations to variables and function parameters
3. Define interfaces for cart items and cart structure
4. Implement proper error handling for edge cases
5. Test thoroughly to ensure functionality remains intact

**Learning Outcomes**:

- Experience gradual migration from JS to TS
- Understand common JavaScript runtime errors
- Practice identifying where types prevent bugs
- Learn to maintain functionality while adding safety

**Rewards**:

- 75 XP
- "Legacy Liberator" badge

### Mission 2: "API Response Chaos"

**Scenario**: An external API sometimes returns inconsistent data structures
**Objective**: Create robust TypeScript interfaces and type guards to handle unpredictable data
**Challenges**:

- Missing properties in API responses
- Wrong data types (string vs number)
- Unexpected null values
- Array vs object inconsistencies

**Solution Approach**:

1. Define comprehensive interfaces for expected API responses
2. Create type guards to validate incoming data
3. Implement fallback mechanisms for missing data
4. Use union types for properties that can vary
5. Add proper error handling for malformed responses

**Learning Outcomes**:

- Master interface design for external data
- Practice defensive programming with type guards
- Learn to handle real-world API inconsistencies
- Understand importance of data validation

**Rewards**:

- 100 XP
- "Data Defender" badge

## "Library Typing Expeditions"

### Expedition 1: "Simple Utility Library"

**Scenario**: Your team uses a small utility library without TypeScript definitions
**Objective**: Create declaration files (.d.ts) for the library
**Library Functions**:

- `formatCurrency(amount: number): string`
- `generateId(): string`
- `deepClone(obj: any): any`
- `debounce(func: Function, delay: number): Function`

**Typing Process**:

1. Analyze library documentation and source code
2. Create interface declarations for complex objects
3. Define function signatures with proper parameter and return types
4. Handle generic functions appropriately
5. Test declarations with sample usage code

**Learning Outcomes**:

- Understand purpose of declaration files
- Practice reading library documentation for typing
- Learn to contribute to DefinitelyTyped
- Gain experience with complex type definitions

**Rewards**:

- 125 XP
- "Typing Explorer" badge

### Expedition 2: "Configuration Object Typing"

**Scenario**: Create TypeScript interfaces for a complex application configuration object
**Objective**: Design comprehensive types for nested configuration structures
**Configuration Structure**:

```javascript
{
  api: {
    baseUrl: string,
    timeout: number,
    retries: number,
    auth: {
      type: 'apiKey' | 'oauth',
      key?: string,
      token?: string
    }
  },
  ui: {
    theme: 'light' | 'dark',
    animations: boolean,
    language: string
  },
  features: {
    analytics: boolean,
    notifications: {
      email: boolean,
      push: boolean,
      sms: boolean
    }
  }
}
```

**Typing Approach**:

1. Break down complex object into modular interfaces
2. Use optional properties appropriately
3. Implement union types for enum-like values
4. Create nested interfaces for logical grouping
5. Document types with JSDoc comments

**Learning Outcomes**:

- Master complex interface design
- Practice modular type architecture
- Learn to handle optional and conditional properties
- Understand union types for restricted values

**Rewards**:

- 100 XP
- "Interface Architect" badge

## "Runtime Error Prevention Labs"

### Lab 1: "The Great TypeError Hunt"

**Scenario**: A production JavaScript application with 10 common runtime errors
**Objective**: Identify errors and show how TypeScript would prevent them
**Common Errors to Find**:

1. Calling methods on undefined objects
2. Accessing properties that don't exist
3. Passing wrong argument types to functions
4. Concatenating strings with numbers unexpectedly
5. Using array methods on non-array values

**Prevention Strategy**:

1. Identify each error in the JavaScript code
2. Show equivalent TypeScript code with proper typing
3. Explain how TypeScript catches each error at compile time
4. Demonstrate the error messages TypeScript would provide
5. Refactor code to be type-safe

**Learning Outcomes**:

- Recognize common JavaScript runtime errors
- Understand how TypeScript prevents these errors
- Learn to interpret TypeScript error messages
- Practice refactoring unsafe code

**Rewards**:

- 80 XP per error identified and prevented
- "Bug Hunter" badge for completing all 10

### Lab 2: "Framework Integration Safety"

**Scenario**: Integrating TypeScript with a popular frontend framework (React/Vue/etc.)
**Objective**: Demonstrate type safety benefits in component-based architecture
**Activities**:

1. Type component props and state
2. Create interfaces for complex data structures
3. Implement type-safe event handlers
4. Use generics for reusable components
5. Validate form inputs with type guards

**Learning Outcomes**:

- Apply TypeScript to component-based development
- Practice typing complex data flows
- Understand framework-specific typing patterns
- Learn to leverage TypeScript in modern development workflows

**Rewards**:

- 150 XP
- "Framework Typist" badge

## "Professional Development Simulations"

### Simulation 1: "Code Review with TypeScript"

**Scenario**: Participate in a professional code review focusing on type safety
**Objective**: Evaluate code for TypeScript best practices and type safety
**Review Checklist**:

- Proper type annotations for all variables/functions
- Appropriate use of interfaces vs types
- Minimal use of `any` type
- Correct handling of nullable values
- Effective use of generics where applicable
- Clear separation of concerns in type definitions

**Process**:

1. Review provided TypeScript code snippet
2. Identify areas for improvement in type safety
3. Suggest specific typing enhancements
4. Provide explanations for recommendations
5. Rate overall type safety of the code

**Learning Outcomes**:

- Develop critical evaluation skills for TypeScript code
- Learn professional code review practices
- Understand industry standards for type safety
- Practice giving constructive feedback

**Rewards**:

- 90 XP
- "Code Critic" badge

### Simulation 2: "TypeScript Migration Planning"

**Scenario**: Plan the migration of a medium-sized JavaScript project to TypeScript
**Objective**: Create a strategic approach for adopting TypeScript in an existing codebase
**Planning Components**:

1. Assessment of current codebase complexity
2. Prioritization of modules for migration
3. Identification of potential challenges
4. Timeline and resource allocation
5. Risk mitigation strategies

**Deliverables**:

1. Migration roadmap document
2. Type safety goals and metrics
3. Team training requirements
4. Tooling and configuration plans
5. Success measurement criteria

**Learning Outcomes**:

- Understand enterprise TypeScript adoption
- Practice strategic planning skills
- Learn to communicate TypeScript benefits to stakeholders
- Gain experience with large-scale migrations

**Rewards**:

- 200 XP
- "Migration Master" badge
