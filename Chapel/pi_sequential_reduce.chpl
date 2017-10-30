use Random;
use Time;

proc main() {
    param n = 10000000;
    const rng = makeRandomStream(real, parSafe=false);
    proc f(): int {
        const x = rng.getNext();
        const y = rng.getNext();
        return if x * x + y * y <= 1.0 then 1 else 0;
    }
    var timer: Timer;
    timer.start();
    const pi = 4.0 * (+ reduce for i in 0..n do f()) / n;
    timer.stop();
    writef("\tSequential Reduce: π ≅ %.11r, calculated in %.2rs, using %i points.\n", pi, timer.elapsed(), n);
}
