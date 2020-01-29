class TestOne {

    public static void main(String[] args) {
        SpiralMatrixLeetcode solution = new SpiralMatrixLeetcode();;
        Data data = new Data();;
     
        Integer num_tests = 100000;
        long tic = System.currentTimeMillis();

        for (int i = 0; i < num_tests; i++)
            for (int[][] input : data.inputs) 
                solution.spiralOrder(input);

        long toc = System.currentTimeMillis();

        System.out.println(toc-tic + " ms with " + num_tests + " tests");
    }
}
