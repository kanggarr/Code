public class FullTimeWorker extends Worker{

    private int hours_Worked;

    FullTimeWorker(String name, double salary_rate, int hours_Worked){
        super(name, salary_rate);
        this.hours_Worked = hours_Worked;
    }

    @Override
    public double computePay() {
        return 100 * hours_Worked;
    }
    
}
