"use client";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-16">
        <h1 className="text-5xl font-bold text-center text-indigo-900 mb-4">
          NexTrip
        </h1>
        <p className="text-xl text-center text-indigo-700 mb-12">
          Constraint-Driven Travel Planner for HackCellence 2026
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          {/* Solo Mode Card */}
          <div className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold text-indigo-900 mb-4">Solo Mode</h2>
            <p className="text-gray-700 mb-6">
              Plan your perfect trip. Set your destination, dates, and budget. Our optimizer creates the best itinerary for you.
            </p>
            <a
              href="/solo"
              className="inline-block bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-6 rounded-lg transition"
            >
              Plan Solo Trip
            </a>
          </div>

          {/* Group Mode Card */}
          <div className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold text-indigo-900 mb-4">Group Mode</h2>
            <p className="text-gray-700 mb-6">
              Travel with friends. Create a session, invite members, and let our Smart-Split algorithm handle fair cost distribution.
            </p>
            <a
              href="/trip"
              className="inline-block bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-6 rounded-lg transition"
            >
              Plan Group Trip
            </a>
          </div>
        </div>

        <div className="mt-16 bg-white rounded-lg shadow-lg p-8 max-w-2xl mx-auto">
          <h2 className="text-2xl font-bold text-indigo-900 mb-4">How It Works</h2>
          <ul className="space-y-3 text-gray-700">
            <li className="flex items-start">
              <span className="inline-block w-6 h-6 bg-indigo-600 text-white rounded-full text-center leading-6 mr-4 flex-shrink-0">1</span>
              <span>Set your destination, dates, and budget constraints</span>
            </li>
            <li className="flex items-start">
              <span className="inline-block w-6 h-6 bg-indigo-600 text-white rounded-full text-center leading-6 mr-4 flex-shrink-0">2</span>
              <span>Our algorithms optimize flights, hotels, and activities</span>
            </li>
            <li className="flex items-start">
              <span className="inline-block w-6 h-6 bg-indigo-600 text-white rounded-full text-center leading-6 mr-4 flex-shrink-0">3</span>
              <span>Get a complete itinerary that maximizes quality within your budget</span>
            </li>
            <li className="flex items-start">
              <span className="inline-block w-6 h-6 bg-indigo-600 text-white rounded-full text-center leading-6 mr-4 flex-shrink-0">4</span>
              <span>Proceed to checkout (mock payments for demo)</span>
            </li>
          </ul>
        </div>
      </div>
    </main>
  );
}
