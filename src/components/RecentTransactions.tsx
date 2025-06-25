
import { Badge } from "@/components/ui/badge";
import { ArrowUpRight, ArrowDownRight, CreditCard, Banknote } from "lucide-react";

const transactions = [
  {
    id: 1,
    type: 'expense',
    category: 'Продукты',
    description: 'Покупка в Пятерочке',
    amount: -2450,
    date: '2024-01-15',
    icon: <ArrowDownRight className="h-4 w-4" />
  },
  {
    id: 2,
    type: 'income',
    category: 'Зарплата',
    description: 'Поступление от работодателя',
    amount: 85000,
    date: '2024-01-15',
    icon: <ArrowUpRight className="h-4 w-4" />
  },
  {
    id: 3,
    type: 'expense',
    category: 'Транспорт',
    description: 'Метро',
    amount: -120,
    date: '2024-01-14',
    icon: <ArrowDownRight className="h-4 w-4" />
  },
  {
    id: 4,
    type: 'expense',
    category: 'Развлечения',
    description: 'Кинотеатр',
    amount: -800,
    date: '2024-01-13',
    icon: <ArrowDownRight className="h-4 w-4" />
  },
  {
    id: 5,
    type: 'income',
    category: 'Фриланс',
    description: 'Проект веб-дизайна',
    amount: 15000,
    date: '2024-01-12',
    icon: <ArrowUpRight className="h-4 w-4" />
  },
];

const RecentTransactions = () => {
  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('ru-RU', {
      style: 'currency',
      currency: 'RUB',
      minimumFractionDigits: 0,
    }).format(Math.abs(amount));
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('ru-RU', {
      day: '2-digit',
      month: '2-digit',
    });
  };

  return (
    <div className="space-y-4">
      {transactions.map((transaction) => (
        <div 
          key={transaction.id}
          className="flex items-center justify-between p-4 bg-slate-50/80 rounded-lg border transition-all duration-200 hover:bg-slate-100/80"
        >
          <div className="flex items-center gap-4">
            <div className={`p-2 rounded-full ${
              transaction.type === 'income' 
                ? 'bg-green-100 text-green-600' 
                : 'bg-red-100 text-red-600'
            }`}>
              {transaction.icon}
            </div>
            <div>
              <p className="font-medium text-slate-900">{transaction.description}</p>
              <div className="flex items-center gap-2 mt-1">
                <Badge variant="secondary" className="text-xs">
                  {transaction.category}
                </Badge>
                <span className="text-xs text-slate-500">{formatDate(transaction.date)}</span>
              </div>
            </div>
          </div>
          <div className="text-right">
            <p className={`font-semibold ${
              transaction.type === 'income' ? 'text-green-600' : 'text-red-600'
            }`}>
              {transaction.type === 'income' ? '+' : '-'}{formatCurrency(transaction.amount)}
            </p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default RecentTransactions;
