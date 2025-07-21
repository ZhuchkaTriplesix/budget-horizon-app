
import { useState } from "react";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { CalendarIcon, Plus } from "lucide-react";
import { Calendar } from "@/components/ui/calendar";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { format } from "date-fns";
import { ru } from "date-fns/locale";
import { cn } from "@/lib/utils";
import { toast } from "@/hooks/use-toast";

interface AddTransactionDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  onSubmit?: (transaction: TransactionData) => Promise<void>;
}

interface TransactionData {
  type: 'income' | 'expense';
  amount: number;
  category: string;
  description: string;
  date: Date;
}

interface ValidationErrors {
  amount?: string;
  category?: string;
  description?: string;
}

const categories = {
  income: ['Зарплата', 'Фриланс', 'Инвестиции', 'Подарки', 'Прочие доходы'],
  expense: ['Продукты', 'Транспорт', 'Жилье', 'Развлечения', 'Здоровье', 'Образование', 'Одежда', 'Прочие расходы']
};

const AddTransactionDialog = ({ open, onOpenChange, onSubmit }: AddTransactionDialogProps) => {
  const [type, setType] = useState<'income' | 'expense'>('expense');
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('');
  const [description, setDescription] = useState('');
  const [date, setDate] = useState<Date>(new Date());
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [errors, setErrors] = useState<ValidationErrors>({});

  const validateForm = (): boolean => {
    const newErrors: ValidationErrors = {};
    
    if (!amount || isNaN(Number(amount)) || Number(amount) <= 0) {
      newErrors.amount = "Введите корректную сумму больше нуля";
    }
    
    if (!category) {
      newErrors.category = "Выберите категорию";
    }
    
    if (!description.trim()) {
      newErrors.description = "Введите описание";
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const resetForm = () => {
    setAmount('');
    setCategory('');
    setDescription('');
    setDate(new Date());
    setErrors({});
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }

    setIsSubmitting(true);
    
    try {
      const transactionData: TransactionData = {
        type,
        amount: Number(amount),
        category,
        description: description.trim(),
        date
      };

      if (onSubmit) {
        await onSubmit(transactionData);
      }

      toast({
        title: "Операция добавлена",
        description: `${type === 'income' ? 'Доход' : 'Расход'} на сумму ${amount} ₽ успешно добавлен`,
      });

      resetForm();
      onOpenChange(false);
    } catch (error) {
      console.error('Error saving transaction:', error);
      toast({
        title: "Ошибка",
        description: "Не удалось сохранить операцию. Попробуйте позже.",
        variant: "destructive"
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-[500px]">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <Plus className="h-5 w-5" />
            Добавить операцию
          </DialogTitle>
          <DialogDescription>
            Создайте новую финансовую операцию для отслеживания доходов и расходов
          </DialogDescription>
        </DialogHeader>

        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Тип операции */}
          <div className="space-y-2">
            <Label>Тип операции</Label>
            <Select value={type} onValueChange={(value: 'income' | 'expense') => setType(value)}>
              <SelectTrigger>
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="income">Доход</SelectItem>
                <SelectItem value="expense">Расход</SelectItem>
              </SelectContent>
            </Select>
          </div>

          {/* Сумма */}
          <div className="space-y-2">
            <Label htmlFor="amount">Сумма *</Label>
            <div className="relative">
              <Input
                id="amount"
                type="number"
                placeholder="0"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                className={cn("pr-8", errors.amount && "border-red-500")}
                aria-invalid={!!errors.amount}
                aria-describedby={errors.amount ? "amount-error" : undefined}
              />
              <span className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500">₽</span>
            </div>
            {errors.amount && (
              <p id="amount-error" className="text-sm text-red-500 mt-1">{errors.amount}</p>
            )}
          </div>

          {/* Категория */}
          <div className="space-y-2">
            <Label>Категория *</Label>
            <Select 
              value={category} 
              onValueChange={setCategory}
            >
              <SelectTrigger className={cn(errors.category && "border-red-500")}>
                <SelectValue placeholder="Выберите категорию" />
              </SelectTrigger>
              <SelectContent>
                {categories[type].map((cat) => (
                  <SelectItem key={cat} value={cat}>
                    {cat}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
            {errors.category && (
              <p className="text-sm text-red-500 mt-1">{errors.category}</p>
            )}
          </div>

          {/* Описание */}
          <div className="space-y-2">
            <Label htmlFor="description">Описание *</Label>
            <Textarea
              id="description"
              placeholder="Опишите операцию..."
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className={cn(errors.description && "border-red-500")}
              rows={3}
            />
            {errors.description && (
              <p className="text-sm text-red-500 mt-1">{errors.description}</p>
            )}
          </div>

          {/* Дата */}
          <div className="space-y-2">
            <Label>Дата</Label>
            <Popover>
              <PopoverTrigger asChild>
                <Button
                  variant="outline"
                  className={cn(
                    "w-full justify-start text-left font-normal",
                    !date && "text-muted-foreground"
                  )}
                >
                  <CalendarIcon className="mr-2 h-4 w-4" />
                  {date ? format(date, 'PPP', { locale: ru }) : <span>Выберите дату</span>}
                </Button>
              </PopoverTrigger>
              <PopoverContent className="w-auto p-0" align="start">
                <Calendar
                  mode="single"
                  selected={date}
                  onSelect={(date) => date && setDate(date)}
                  initialFocus
                />
              </PopoverContent>
            </Popover>
          </div>

          <div className="flex justify-end gap-3">
            <Button type="button" variant="outline" onClick={() => onOpenChange(false)}>
              Отмена
            </Button>
            <Button type="submit" disabled={isSubmitting}>
              {isSubmitting ? "Сохранение..." : "Сохранить"}
            </Button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
};

export default AddTransactionDialog;
