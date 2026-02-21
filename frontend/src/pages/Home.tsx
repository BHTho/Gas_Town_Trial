const Home = () => {
  return (
    <div className="py-12">
      <div className="text-center">
        <h1 className="text-5xl font-bold text-gray-900 mb-6">
          Welcome to <span className="text-indigo-600">Vuestic-inspired</span> Theme
        </h1>
        <p className="text-xl text-gray-700 max-w-3xl mx-auto mb-10">
          This is a modern web application built with Vite, React, TypeScript, Tailwind CSS, and inspired by Vuestic UI design system.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto mt-16">
          <div className="bg-white p-8 rounded-2xl shadow-lg border border-gray-100">
            <div className="text-indigo-600 text-4xl mb-4">⚡</div>
            <h3 className="text-2xl font-bold text-gray-900 mb-4">Vite</h3>
            <p className="text-gray-600">Lightning fast build tool and dev server with instant HMR.</p>
          </div>
          <div className="bg-white p-8 rounded-2xl shadow-lg border border-gray-100">
            <div className="text-indigo-600 text-4xl mb-4">🧬</div>
            <h3 className="text-2xl font-bold text-gray-900 mb-4">React + TypeScript</h3>
            <p className="text-gray-600">Type-safe components with modern React patterns.</p>
          </div>
          <div className="bg-white p-8 rounded-2xl shadow-lg border border-gray-100">
            <div className="text-indigo-600 text-4xl mb-4">🎨</div>
            <h3 className="text-2xl font-bold text-gray-900 mb-4">Tailwind CSS</h3>
            <p className="text-gray-600">Utility-first CSS framework with Vuestic-inspired design tokens.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;