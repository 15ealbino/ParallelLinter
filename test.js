(testMethod = x => {
    console.log(x)
})(1);

class Test {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    getVals( {
        console.log(this.x)
        console.log(this.y)
    }
}