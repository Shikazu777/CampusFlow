function UpcomingEvents() {
  const events = [
    "Tech Symposium",
    "Hackathon 2026",
    "Cultural Fest"
  ];

  return (
    <div className="bg-slate-800 rounded-3xl p-6">

      <h2 className="text-2xl font-bold mb-6">
        Upcoming Events
      </h2>

      <div className="space-y-4">

        {events.map((event) => (
          <div
            key={event}
            className="
              bg-slate-700
              p-4
              rounded-2xl
            "
          >
            {event}
          </div>
        ))}

      </div>

    </div>
  );
}

export default UpcomingEvents;