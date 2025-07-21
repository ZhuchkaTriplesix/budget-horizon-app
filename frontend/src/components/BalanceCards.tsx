
import { Card, CardContent } from "@/components/ui/card";
import { Wallet, TrendingUp, TrendingDown } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import { useMemo } from "react";

interface BalanceCardsProps {
  totalBalance: number;
  monthlyIncome: number;
  monthlyExpenses: number;
  showBalance: boolean;
  isLoading?: boolean;
}

const formatCurrency = (amount: number, hideAmount: boolean): string => {
  if (hideAmount) return "••••••";
  
  try {
    return new Intl.NumberFormat('ru-RU', {
      style: 'currency',
      currency: 'RUB',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(amount);
  } catch (error) {
    console.error('Error formatting currency:', error);
    return '0 ₽';
  }
};

const BalanceCardSkeleton = () => (
  <Card className="border-0 shadow-lg bg-gradient-to-br from-slate-100 to-slate-200">
    <CardContent className="p-6">
      <div className="flex items-center justify-between">
        <div>
          <div className="w-24 h-4 bg-slate-300 rounded mb-3" />
          <div className="w-32 h-6 bg-slate-300 rounded" />
        </div>
        <div className="w-8 h-8 bg-slate-300 rounded-full" />
      </div>
    </CardContent>
  </Card>
);

const BalanceCards = ({ 
  totalBalance, 
  monthlyIncome, 
  monthlyExpenses, 
  showBalance,
  isLoading = false 
}: BalanceCardsProps) => {
  const monthlyDiff = useMemo(() => 
    monthlyIncome - monthlyExpenses
  , [monthlyIncome, monthlyExpenses]);

  if (isLoading) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6">
        <BalanceCardSkeleton />
        <BalanceCardSkeleton />
        <BalanceCardSkeleton />
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6">
      <Card className="border-0 shadow-lg bg-gradient-to-br from-blue-600 to-indigo-600 text-white transform transition-all duration-300 hover:scale-105">
        <CardContent className="p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-blue-100 text-sm font-medium">Общий баланс</p>
              <p className="text-2xl sm:text-3xl font-bold mt-2">
                {formatCurrency(totalBalance, !showBalance)}
              </p>
            </div>
            <Wallet className="h-8 w-8 text-blue-200" />
          </div>
        </CardContent>
      </Card>

      <Card className="border-0 shadow-lg bg-gradient-to-br from-green-500 to-emerald-600 text-white transform transition-all duration-300 hover:scale-105">
        <CardContent className="p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-green-100 text-sm font-medium">Доходы за месяц</p>
              <p className="text-2xl sm:text-3xl font-bold mt-2">
                {formatCurrency(monthlyIncome, !showBalance)}
              </p>
            </div>
            <TrendingUp className="h-8 w-8 text-green-200" />
          </div>
        </CardContent>
      </Card>

      <Card className="border-0 shadow-lg bg-gradient-to-br from-red-500 to-rose-600 text-white transform transition-all duration-300 hover:scale-105">
        <CardContent className="p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-red-100 text-sm font-medium">Расходы за месяц</p>
              <p className="text-2xl sm:text-3xl font-bold mt-2">
                {formatCurrency(monthlyExpenses, !showBalance)}
              </p>
              <p className={`text-sm mt-2 ${monthlyDiff >= 0 ? 'text-green-200' : 'text-red-200'}`}>
                {monthlyDiff >= 0 ? 'Профицит: ' : 'Дефицит: '}
                {formatCurrency(Math.abs(monthlyDiff), !showBalance)}
              </p>
            </div>
            <TrendingDown className="h-8 w-8 text-red-200" />
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default BalanceCards;
