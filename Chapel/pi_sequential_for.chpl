use Random;
use Time;

proc main() {
    param n = 10000000;
    const index_range = {0..n};
    const rng_x = makeRandomStream(real, parSafe=false);
    const rng_y = makeRandomStream(real, parSafe=false);
    var sum: int = 0;
    var timer: Timer;
    timer.start();
    for (i, r_x, r_y) in zip(index_range, rng_x.iterate(index_range), rng_y.iterate(index_range)) {
        sum += if r_x * r_x + r_y * r_y <= 1.0 then 1 else 0;
    }
    const pi = 4.0 * sum / n;
    timer.stop();
    writef("\tSequential For: π ≅ %.11r, calculated in %.2rs, using %i points.\n", pi, timer.elapsed(), n);
}
