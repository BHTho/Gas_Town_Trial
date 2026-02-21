export default function HomePage() {
  return (
    <div className="py-8">
      <h1 className="text-3xl font-bold text-primary-900 mb-4">Home</h1>
      <p className="text-gray-700 mb-6">
        Welcome to the Gas Town SS frontend. This is the home page demonstrating routing and vuestic-inspired theme.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-md">
          <h2 className="text-xl font-semibold text-primary-800 mb-2">Features</h2>
          <ul className="list-disc pl-5 text-gray-700">
            <li>Vite + React + TypeScript</li>
            <li>Tailwind CSS with custom vuestic-inspired theme</li>
            <li>React Router for navigation</li>
            <li>Responsive design</li>
            <li>Component-based architecture</li>
          </ul>
        </div>
        <div className="bg-white p-6 rounded-xl shadow-md">
          <h2 className="text-xl font-semibold text-primary-800 mb-2">Getting Started</h2>
          <p className="text-gray-700 mb-4">
            Explore the navigation menu to see different pages and layouts.
          </p>
          <button className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors">
            Learn More
          </button>
        </div>
      </div>
    </div>
  )
}