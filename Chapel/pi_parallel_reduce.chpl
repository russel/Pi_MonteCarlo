use Random;
use Time;

proc main() {
    param n = 10000000;
    const rng = makeRandomStream(real);
    proc f(): int {
        const x = rng.getNext();
        const y = rng.getNext();
        return if x * x + y * y <= 1.0 then 1 else 0;
    }
    var timer: Timer;
    timer.start();
    const pi = 4.0 * (+ reduce [i in 0..n] f()) / n;
    timer.stop();
    writef("\tParallel Reduce: π ≅ %.11r, calculated in %.2rs, using %i points, on %i processing units.\n", pi, timer.elapsed(), n, here.numPUs());
}
