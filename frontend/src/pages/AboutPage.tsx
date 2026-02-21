export default function AboutPage() {
  return (
    <div className="py-8">
      <h1 className="text-3xl font-bold text-primary-900 mb-4">About</h1>
      <p className="text-gray-700 mb-6">
        This frontend is part of the Gas Town SS project, built with modern web technologies and a vuestic-inspired design system.
      </p>
      <div className="bg-white p-6 rounded-xl shadow-md mb-6">
        <h2 className="text-xl font-semibold text-primary-800 mb-2">Technology Stack</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4">
          <div className="text-center p-4 bg-primary-50 rounded-lg">
            <div className="text-primary-700 font-bold">Vite</div>
            <div className="text-sm text-gray-600">Build tool</div>
          </div>
          <div className="text-center p-4 bg-success-50 rounded-lg">
            <div className="text-success-700 font-bold">React</div>
            <div className="text-sm text-gray-600">UI library</div>
          </div>
          <div className="text-center p-4 bg-warning-50 rounded-lg">
            <div className="text-warning-700 font-bold">TypeScript</div>
            <div className="text-sm text-gray-600">Type safety</div>
          </div>
          <div className="text-center p-4 bg-info-50 rounded-lg">
            <div className="text-info-700 font-bold">Tailwind CSS</div>
            <div className="text-sm text-gray-600">Styling</div>
          </div>
        </div>
      </div>
      <div className="bg-white p-6 rounded-xl shadow-md">
        <h2 className="text-xl font-semibold text-primary-800 mb-2">Vuestic-inspired Theme</h2>
        <p className="text-gray-700">
          The color palette is inspired by Vuestic UI, providing a consistent design system with primary, secondary, success, info, warning, and danger colors.
        </p>
      </div>
    </div>
  )
}