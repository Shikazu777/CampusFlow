function CommunityPreview() {
  return (
    <div className="bg-slate-800 rounded-3xl p-6">

      <div className="flex justify-between mb-6">
        <h2 className="text-2xl font-bold">
          Community Feed
        </h2>

        <button className="text-blue-400">
          View All
        </button>
      </div>

      <div className="bg-slate-700 rounded-2xl p-5">

        <div className="flex items-center gap-3">

          <div className="
            h-12
            w-12
            rounded-full
            bg-purple-500
            flex
            items-center
            justify-center
          ">
            D
          </div>

          <div>
            <h3 className="font-semibold">
              Dhanraj
            </h3>

            <p className="text-slate-400 text-sm">
              2 hours ago
            </p>
          </div>

        </div>

        <p className="mt-5">
          Anyone attending the Hackathon next week?
        </p>

        <div className="
          flex
          gap-6
          mt-5
          text-slate-400
        ">
          <span>👍 42</span>
          <span>💬 12</span>
        </div>

      </div>

    </div>
  );
}

export default CommunityPreview;