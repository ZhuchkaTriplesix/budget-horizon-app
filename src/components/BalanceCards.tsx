
import { Card, CardContent } from "@/components/ui/card";
import { TrendingUp, TrendingDown, Wallet } from "lucide-react";

interface BalanceCardsProps {
  totalBalance: number;
  monthlyIncome: number;
  monthlyExpenses: number;
  showBalance: boolean;
}

const BalanceCards = ({ totalBalance, monthlyIncome, monthlyExpenses, showBalance }: BalanceCardsProps) => {
  const formatCurrency = (amount: number) => {
    if (!showBalance) return "••••••";
    return new Intl.NumberFormat('ru-RU', {
      style: 'currency',
      currency: 'RUB',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(amount);
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6">
      <Card className="border-0 shadow-lg bg-gradient-to-br from-blue-600 to-indigo-600 text-white transform transition-all duration-300 hover:scale-105">
        <CardContent className="p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-blue-100 text-sm font-medium">Общий баланс</p>
              <p className="text-2xl sm:text-3xl font-bold mt-2">{formatCurrency(totalBalance)}</p>
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
              <p className="text-2xl sm:text-3xl font-bold mt-2">{formatCurrency(monthlyIncome)}</p>
            </div>
            <TrendingUp className="h-8 w-8 text-green-200" />
          </div>
        </CardContent>
      </Card>

      <Card className="border-0 shadow-lg bg-gradient-to-br from-red-500 to-pink-600 text-white transform transition-all duration-300 hover:scale-105">
        <CardContent className="p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-red-100 text-sm font-medium">Расходы за месяц</p>
              <p className="text-2xl sm:text-3xl font-bold mt-2">{formatCurrency(monthlyExpenses)}</p>
            </div>
            <TrendingDown className="h-8 w-8 text-red-200" />
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default BalanceCards;
