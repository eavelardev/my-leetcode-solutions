import java.util.*;

class TestData {

    public static void main(String[] args) {
        SpiralMatrixLeetcode solution = new SpiralMatrixLeetcode();;
        Data data = new Data();;

        for (int i = 0; i < data.inputs.length; i++) 
            if (!solution.spiralOrder(data.inputs[i]).equals(Arrays.asList(data.outputs[i]))) {
                System.out.println("Fail in test: " + i);
                System.exit(0);
            }    
                   
        System.out.println("OK!");
    }
}
