
import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Plus, TrendingUp, TrendingDown, Wallet, CreditCard, PiggyBank, Eye, EyeOff } from "lucide-react";
import BalanceCards from "@/components/BalanceCards";
import ExpenseChart from "@/components/ExpenseChart";
import IncomeExpenseChart from "@/components/IncomeExpenseChart";
import RecentTransactions from "@/components/RecentTransactions";
import AddTransactionDialog from "@/components/AddTransactionDialog";

const Index = () => {
  const [showBalance, setShowBalance] = useState(true);
  const [isAddTransactionOpen, setIsAddTransactionOpen] = useState(false);

  const toggleBalanceVisibility = () => {
    setShowBalance(!showBalance);
  };

  const totalBalance = 125750.50;
  const monthlyIncome = 85000;
  const monthlyExpenses = 52340;

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50 p-4 sm:p-6">
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Header */}
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
          <div>
            <h1 className="text-3xl sm:text-4xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              FinanceFlow
            </h1>
            <p className="text-slate-600 mt-1">Управление личными финансами</p>
          </div>
          <div className="flex gap-3">
            <Button
              variant="outline"
              size="sm"
              onClick={toggleBalanceVisibility}
              className="flex items-center gap-2"
            >
              {showBalance ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
              {showBalance ? "Скрыть" : "Показать"}
            </Button>
            <Button 
              onClick={() => setIsAddTransactionOpen(true)}
              className="flex items-center gap-2 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700"
            >
              <Plus className="h-4 w-4" />
              Добавить операцию
            </Button>
          </div>
        </div>

        {/* Balance Cards */}
        <BalanceCards 
          totalBalance={totalBalance}
          monthlyIncome={monthlyIncome}
          monthlyExpenses={monthlyExpenses}
          showBalance={showBalance}
        />

        {/* Main Content */}
        <Tabs defaultValue="overview" className="space-y-6">
          <TabsList className="grid w-full grid-cols-4 lg:w-fit lg:grid-cols-4">
            <TabsTrigger value="overview">Обзор</TabsTrigger>
            <TabsTrigger value="analytics">Аналитика</TabsTrigger>
            <TabsTrigger value="loans">Кредиты</TabsTrigger>
            <TabsTrigger value="deposits">Вклады</TabsTrigger>
          </TabsList>

          <TabsContent value="overview" className="space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Income vs Expenses Chart */}
              <Card className="border-0 shadow-lg bg-white/70 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <TrendingUp className="h-5 w-5 text-green-600" />
                    Доходы и расходы
                  </CardTitle>
                  <CardDescription>Динамика за последние 6 месяцев</CardDescription>
                </CardHeader>
                <CardContent>
                  <IncomeExpenseChart />
                </CardContent>
              </Card>

              {/* Expense Categories */}
              <Card className="border-0 shadow-lg bg-white/70 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <TrendingDown className="h-5 w-5 text-red-500" />
                    Расходы по категориям
                  </CardTitle>
                  <CardDescription>Распределение трат за текущий месяц</CardDescription>
                </CardHeader>
                <CardContent>
                  <ExpenseChart />
                </CardContent>
              </Card>
            </div>

            {/* Recent Transactions */}
            <Card className="border-0 shadow-lg bg-white/70 backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Wallet className="h-5 w-5 text-blue-600" />
                  Последние операции
                </CardTitle>
                <CardDescription>Ваши недавние финансовые операции</CardDescription>
              </CardHeader>
              <CardContent>
                <RecentTransactions />
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="analytics" className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <Card className="border-0 shadow-lg bg-white/70 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle>Средние расходы</CardTitle>
                  <CardDescription>За день</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-red-600">₽1,745</div>
                  <p className="text-sm text-slate-600 mt-1">+12% к прошлому месяцу</p>
                </CardContent>
              </Card>

              <Card className="border-0 shadow-lg bg-white/70 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle>Экономия</CardTitle>
                  <CardDescription>За месяц</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-green-600">₽32,660</div>
                  <p className="text-sm text-slate-600 mt-1">38% от доходов</p>
                </CardContent>
              </Card>

              <Card className="border-0 shadow-lg bg-white/70 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle>Самая затратная категория</CardTitle>
                  <CardDescription>Текущий месяц</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="text-lg font-semibold">Продукты</div>
                  <div className="text-xl font-bold text-orange-600">₽18,450</div>
                  <Badge variant="secondary" className="mt-2">35% расходов</Badge>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          <TabsContent value="loans" className="space-y-6">
            <Card className="border-0 shadow-lg bg-white/70 backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <CreditCard className="h-5 w-5 text-orange-600" />
                  Активные кредиты
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div className="p-4 bg-gradient-to-r from-orange-50 to-red-50 rounded-lg border">
                    <h3 className="font-semibold">Ипотека</h3>
                    <p className="text-sm text-slate-600">Остаток: ₽2,450,000</p>
                    <p className="text-sm text-slate-600">Ежемесячный платеж: ₽32,500</p>
                    <div className="mt-2">
                      <div className="w-full bg-slate-200 rounded-full h-2">
                        <div className="bg-orange-600 h-2 rounded-full" style={{width: '68%'}}></div>
                      </div>
                      <p className="text-xs text-slate-500 mt-1">Выплачено 68%</p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="deposits" className="space-y-6">
            <Card className="border-0 shadow-lg bg-white/70 backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <PiggyBank className="h-5 w-5 text-green-600" />
                  Вклады и накопления
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  <div className="p-4 bg-gradient-to-r from-green-50 to-emerald-50 rounded-lg border">
                    <h3 className="font-semibold">Накопительный счет</h3>
                    <p className="text-sm text-slate-600">Баланс: ₽125,000</p>
                    <p className="text-sm text-slate-600">Процентная ставка: 8.5% годовых</p>
                    <p className="text-sm text-green-600 font-medium">Начислено за месяц: ₽885</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>

        {/* Add Transaction Dialog */}
        <AddTransactionDialog 
          open={isAddTransactionOpen}
          onOpenChange={setIsAddTransactionOpen}
        />
      </div>
    </div>
  );
};

export default Index;
