package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

    private static VendingMachineImpl instance = new VendingMachineImpl();
    private int quarters;

    private VendingMachineImpl() {
    }

    public static VendingMachine getInstance() {
        return instance;
    }

    @Override
    public Drink pressButton(String drinkName) throws NotEnoughMoneyException, UnknownDrinkException {
        if ("ScottCola".equals(drinkName)) {
            if (quarters >= 3) {
                quarters -= 3;
                return new ScottCola();
            } else {
                throw new NotEnoughMoneyException();
            }
        } else if ("KarenTea".equals(drinkName)) {
            if (quarters >= 4) {
                quarters -= 4;
                return new KarenTea();
            } else {
                throw new NotEnoughMoneyException();
            }
        } else {
            throw new UnknownDrinkException();
        }
    }

    @Override
    public void insertQuarter() {
        quarters++;
    }

    private static class ScottCola implements Drink {
        @Override
        public String getName() {
            return "ScottCola";
        }

        @Override
        public boolean isFizzy() {
            return true;
        }
    }

    private static class KarenTea implements Drink {
        @Override
        public String getName() {
            return "KarenTea";
        }

        @Override
        public boolean isFizzy() {
            return false;
        }
    }
}

