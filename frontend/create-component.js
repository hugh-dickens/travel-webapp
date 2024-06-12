const fs = require('fs');
const path = require('path');

const componentName = process.argv[2];

if (!componentName) {
  console.error('Please provide a component name.');
  process.exit(1);
}

const componentDir = path.join(__dirname, 'src', 'components', componentName);

if (fs.existsSync(componentDir)) {
  console.error(`Component ${componentName} already exists.`);
  process.exit(1);
}

fs.mkdirSync(componentDir);

const componentTemplate = `
import React from 'react';
import './${componentName}.css';

const ${componentName} = () => {
  return (
    <div className="${componentName}">
      {/* Your component code here */}
    </div>
  );
};

export default ${componentName};
`;

fs.writeFileSync(path.join(componentDir, `${componentName}.js`), componentTemplate);
fs.writeFileSync(path.join(componentDir, `${componentName}.css`), `/* Styles for ${componentName} */`);

console.log(`Component ${componentName} created successfully.`);
