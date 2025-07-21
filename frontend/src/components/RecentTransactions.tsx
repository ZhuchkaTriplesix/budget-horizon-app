
import { Badge } from "@/components/ui/badge";
import { ArrowUpRight, ArrowDownRight } from "lucide-react";
import { useMemo } from "react";
import { Skeleton } from "@/components/ui/skeleton";

export interface Transaction {
  id: number;
  type: 'income' | 'expense';
  category: string;
  description: string;
  amount: number;
  date: string;
}

interface RecentTransactionsProps {
  transactions?: Transaction[];
  isLoading?: boolean;
}

const formatCurrency = (amount: number): string => {
  try {
    return new Intl.NumberFormat('ru-RU', {
      style: 'currency',
      currency: 'RUB',
      minimumFractionDigits: 0,
    }).format(Math.abs(amount));
  } catch (error) {
    console.error('Error formatting currency:', error);
    return '0 ₽';
  }
};

const formatDate = (dateString: string): string => {
  try {
    return new Date(dateString).toLocaleDateString('ru-RU', {
      day: '2-digit',
      month: '2-digit',
    });
  } catch (error) {
    console.error('Error formatting date:', error);
    return '--/--';
  }
};

const TransactionSkeleton = () => (
  <div className="flex items-center justify-between p-4 bg-slate-50/80 rounded-lg border animate-pulse">
    <div className="flex items-center gap-4">
      <div className="w-8 h-8 bg-slate-200 rounded-full" />
      <div>
        <div className="w-32 h-4 bg-slate-200 rounded mb-2" />
        <div className="w-24 h-3 bg-slate-200 rounded" />
      </div>
    </div>
    <div className="w-20 h-4 bg-slate-200 rounded" />
  </div>
);

const RecentTransactions = ({ transactions = [], isLoading = false }: RecentTransactionsProps) => {
  const sortedTransactions = useMemo(() => {
    return [...transactions].sort((a, b) => 
      new Date(b.date).getTime() - new Date(a.date).getTime()
    );
  }, [transactions]);

  if (isLoading) {
    return (
      <div className="space-y-4">
        {[...Array(5)].map((_, index) => (
          <TransactionSkeleton key={index} />
        ))}
      </div>
    );
  }

  if (transactions.length === 0) {
    return (
      <div className="text-center py-8 text-slate-500">
        Нет транзакций для отображения
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {sortedTransactions.map((transaction) => (
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
              {transaction.type === 'income' 
                ? <ArrowUpRight className="h-4 w-4" /> 
                : <ArrowDownRight className="h-4 w-4" />
              }
            </div>
            <div>
              <p className="font-medium text-slate-900">{transaction.description}</p>
              <div className="flex items-center gap-2 mt-1">
                <Badge variant="secondary" className="text-xs">
                  {transaction.category}
                </Badge>
                <span className="text-xs text-slate-500">
                  {formatDate(transaction.date)}
                </span>
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
