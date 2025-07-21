
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

const data = [
  { month: 'Авг', income: 82000, expenses: 48500 },
  { month: 'Сен', income: 78000, expenses: 52000 },
  { month: 'Окт', income: 85000, expenses: 49800 },
  { month: 'Ноя', income: 87000, expenses: 54200 },
  { month: 'Дек', income: 90000, expenses: 61000 },
  { month: 'Янв', income: 85000, expenses: 52340 },
];

const IncomeExpenseChart = () => {
  const CustomTooltip = ({ active, payload, label }: any) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-white p-3 rounded-lg shadow-lg border">
          <p className="font-semibold">{label}</p>
          {payload.map((entry: any, index: number) => (
            <p key={index} style={{ color: entry.color }}>
              {entry.name}: {new Intl.NumberFormat('ru-RU', {
                style: 'currency',
                currency: 'RUB',
                minimumFractionDigits: 0,
              }).format(entry.value)}
            </p>
          ))}
        </div>
      );
    }
    return null;
  };

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
        <XAxis 
          dataKey="month" 
          stroke="#64748b"
          fontSize={12}
        />
        <YAxis 
          stroke="#64748b"
          fontSize={12}
          tickFormatter={(value) => `${value / 1000}k`}
        />
        <Tooltip content={<CustomTooltip />} />
        <Legend />
        <Bar 
          dataKey="income" 
          name="Доходы"
          fill="#22c55e" 
          radius={[4, 4, 0, 0]}
        />
        <Bar 
          dataKey="expenses" 
          name="Расходы"
          fill="#ef4444" 
          radius={[4, 4, 0, 0]}
        />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default IncomeExpenseChart;
