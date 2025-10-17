# Code Examples

This document contains various code blocks to test Prism.js syntax highlighting.

## Python Code

Here's a Python example:

```python
def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

## JavaScript Code

JavaScript example with ES6 syntax:

```javascript
// Arrow functions and array methods
const numbers = [1, 2, 3, 4, 5];
const squares = numbers
    .filter(n => n % 2 === 0)
    .map(n => n * n);

console.log(squares); // [4, 16]

class Calculator {
    constructor(initial = 0) {
        this.value = initial;
    }
    
    add(x) {
        this.value += x;
        return this;
    }
    
    multiply(x) {
        this.value *= x;
        return this;
    }
}

const calc = new Calculator(5).add(3).multiply(2);
console.log(calc.value); // 16
```

## HTML/CSS Code

HTML structure with CSS:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Example Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Example</h1>
        <p>This is a test page.</p>
    </div>
</body>
</html>
```

## SQL Code

Database query example:

```sql
SELECT 
    u.user_id,
    u.username,
    COUNT(p.post_id) as post_count,
    MAX(p.created_at) as last_post_date
FROM users u
LEFT JOIN posts p ON u.user_id = p.user_id
WHERE u.created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY u.user_id, u.username
HAVING COUNT(p.post_id) > 0
ORDER BY post_count DESC
LIMIT 10;
```

## Bash/Shell Script

Shell scripting example:

```bash
#!/bin/bash

# Backup script
BACKUP_DIR="/backup"
SOURCE_DIR="/data"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

echo "Starting backup at $TIMESTAMP"

if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
fi

tar -czf "$BACKUP_DIR/backup_$TIMESTAMP.tar.gz" "$SOURCE_DIR"

if [ $? -eq 0 ]; then
    echo "Backup completed successfully"
    find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +7 -delete
else
    echo "Backup failed!"
    exit 1
fi
```

## JSON Configuration

JSON data format:

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "A sample project",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "jest",
    "build": "webpack"
  },
  "dependencies": {
    "express": "^4.18.0",
    "lodash": "^4.17.21"
  },
  "devDependencies": {
    "jest": "^29.0.0",
    "webpack": "^5.0.0"
  }
}
```

## Line Numbers Test

Here's a longer code block to test line numbers:

```java
public class BubbleSort {
    /**
     * Sorts an array using bubble sort algorithm
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap elements
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    
    public static void main(String[] args) {
        int[] numbers = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(numbers);
        
        System.out.println("Sorted array:");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
    }
}
```

## Plain Text

Here's a plain text code block (no language specified):

```
This is plain text
It won't have syntax highlighting
But it should still be displayed in a code block
Line 4
Line 5
```

---

That's all for the code examples! Check if the syntax highlighting is applied correctly with the Prism.js themes.
