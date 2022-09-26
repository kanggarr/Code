public class TestManager {
    public static void main(String[] args) {
        Employee emp1 = new Employee("John", 12000);
        Employee emp2 = new Employee("Wiski", 15000);
        Manager mng1 = new Manager("Max", 24000, "DEV");
        System.out.println(emp1);
        System.out.println(emp2);
        System.out.println(mng1);
    }
    
}
