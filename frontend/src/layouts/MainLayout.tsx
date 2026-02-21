import { Outlet, Link } from 'react-router-dom'

export default function MainLayout() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 to-gray-100">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center">
              <Link to="/" className="text-2xl font-bold text-primary-900">
                Gas Town SS
              </Link>
              <nav className="ml-10 flex space-x-4">
                <Link
                  to="/"
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-900 hover:bg-primary-50 transition-colors"
                >
                  Home
                </Link>
                <Link
                  to="/about"
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary-900 hover:bg-primary-50 transition-colors"
                >
                  About
                </Link>
              </nav>
            </div>
            <div>
              <button className="px-4 py-2 bg-primary-600 text-white text-sm font-medium rounded-lg hover:bg-primary-700 transition-colors">
                Dashboard
              </button>
            </div>
          </div>
        </div>
      </header>
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Outlet />
      </main>
      <footer className="bg-white border-t border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-gray-600">
              &copy; {new Date().getFullYear()} Gas Town SS. Built with Vite, React, TypeScript, and Tailwind CSS.
            </p>
            <div className="mt-4 md:mt-0">
              <a
                href="https://vitejs.dev"
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-gray-500 hover:text-primary-700 mx-3"
              >
                Vite
              </a>
              <a
                href="https://react.dev"
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-gray-500 hover:text-primary-700 mx-3"
              >
                React
              </a>
              <a
                href="https://tailwindcss.com"
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-gray-500 hover:text-primary-700 mx-3"
              >
                Tailwind CSS
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}