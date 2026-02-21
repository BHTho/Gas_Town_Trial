import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import './App.css';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        <nav className="bg-white shadow-lg">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex items-center">
                <span className="text-2xl font-bold text-indigo-600">Vuestic</span>
              </div>
              <div className="flex items-center space-x-8">
                <Link to="/" className="text-gray-700 hover:text-indigo-600 font-medium transition-colors">
                  Home
                </Link>
                <Link to="/about" className="text-gray-700 hover:text-indigo-600 font-medium transition-colors">
                  About
                </Link>
                <a
                  href="https://vuestic.dev"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
                >
                  Vuestic UI
                </a>
              </div>
            </div>
          </div>
        </nav>
        <main className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </main>
        <footer className="bg-white border-t mt-12">
          <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
            <p className="text-center text-gray-500">
              Built with Vite + React + TypeScript + Tailwind CSS • Vuestic-inspired theme
            </p>
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;