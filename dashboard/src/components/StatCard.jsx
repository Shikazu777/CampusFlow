function StatCard({
  title,
  value
}) {
  return (
    <div className="
      bg-slate-800
      p-6
      rounded-3xl
      shadow-lg
    ">

      <p className="text-slate-400">
        {title}
      </p>

      <h2 className="
        text-4xl
        font-bold
        mt-3
      ">
        {value}
      </h2>

    </div>
  );
}

export default StatCard;