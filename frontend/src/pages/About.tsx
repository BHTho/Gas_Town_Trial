const About = () => {
  return (
    <div className="py-12">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-5xl font-bold text-gray-900 mb-8">About This Project</h1>
        <div className="prose prose-lg text-gray-700 mb-12">
          <p>
            This project demonstrates a modern frontend setup with <strong>Vite</strong>, <strong>React</strong>, <strong>TypeScript</strong>, and <strong>Tailwind CSS</strong>, featuring a theme inspired by <strong>Vuestic UI</strong>.
          </p>
          <p>
            Vuestic UI is a Vue.js component library, but we've adapted its design language—color palette, spacing, and component styles—to create a consistent React experience.
          </p>
          <p>
            The setup includes:
          </p>
          <ul>
            <li><strong>Routing</strong> with React Router v6</li>
            <li><strong>Tailwind CSS</strong> with custom configuration</li>
            <li><strong>Vuestic UI components</strong> installed for reference</li>
            <li><strong>TypeScript</strong> for type safety</li>
            <li><strong>ESLint</strong> and <strong>PostCSS</strong> configured</li>
          </ul>
          <p>
            The folder structure follows best practices for scalability, with separate directories for pages, components, and layouts.
          </p>
        </div>
        <div className="bg-indigo-50 border-l-4 border-indigo-500 p-6 rounded-r-lg">
          <h3 className="text-xl font-bold text-indigo-800 mb-2">Project Structure</h3>
          <pre className="text-sm bg-white p-4 rounded-lg overflow-auto">
{`frontend/
├── src/
│   ├── pages/          # Route components
│   ├── components/     # Reusable UI components
│   ├── layouts/        # Layout components
│   ├── App.tsx        # Main app with routes
│   └── main.tsx       # Entry point
├── public/            # Static assets
├── index.html         # HTML template
└── *.config.js/ts     # Tooling configs`}
          </pre>
        </div>
      </div>
    </div>
  );
};

export default About;