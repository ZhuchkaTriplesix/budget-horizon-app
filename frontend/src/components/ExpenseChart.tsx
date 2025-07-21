
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts';

interface ExpenseData {
  name: string;
  value: number;
  color: string;
}

interface CustomTooltipProps {
  active?: boolean;
  payload?: Array<{
    name: string;
    value: number;
    color: string;
  }>;
}

const data: ExpenseData[] = [
  { name: 'Продукты', value: 18450, color: '#ef4444' },
  { name: 'Транспорт', value: 8200, color: '#f97316' },
  { name: 'Жилье', value: 12000, color: '#eab308' },
  { name: 'Развлечения', value: 5690, color: '#22c55e' },
  { name: 'Здоровье', value: 4200, color: '#3b82f6' },
  { name: 'Прочее', value: 3800, color: '#8b5cf6' },
];

const ExpenseChart = () => {
  const formatCurrency = (value: number): string => {
    try {
      return new Intl.NumberFormat('ru-RU', {
        style: 'currency',
        currency: 'RUB',
        minimumFractionDigits: 0,
      }).format(value);
    } catch (error) {
      console.error('Error formatting currency:', error);
      return '0 ₽';
    }
  };

  const CustomTooltip = ({ active, payload }: CustomTooltipProps) => {
    if (active && payload && payload.length) {
      const data = payload[0];
      return (
        <div className="bg-white p-3 rounded-lg shadow-lg border" role="tooltip">
          <p className="font-semibold">{data.name}</p>
          <p className="text-blue-600">
            {formatCurrency(data.value)}
          </p>
        </div>
      );
    }
    return null;
  };

  return (
    <ResponsiveContainer width="100%" height={300}>
      <PieChart>
        <Pie
          data={data}
          cx="50%"
          cy="50%"
          outerRadius={80}
          fill="#8884d8"
          dataKey="value"
          label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
          aria-label="Диаграмма расходов по категориям"
        >
          {data.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={entry.color} />
          ))}
        </Pie>
        <Tooltip content={<CustomTooltip />} />
      </PieChart>
    </ResponsiveContainer>
  );
};

export default ExpenseChart;
