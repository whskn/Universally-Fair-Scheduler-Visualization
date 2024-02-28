# Universally-Fair-Scheduler-Visualization
## Visualization script of Universally Fair Scheduler (UFS)
![ufs](https://github.com/whskn/Universally-Fair-Scheduler-Visualization/assets/76423174/6e09fa04-5be6-4abf-ad5c-c6adc4fcb42e)

## Usage
```Usage: python3 cfs.py [N_OF_PROCESSES] [MAX_WEIGHT (optional, default - N_OF_PROCESSES * 2)]```

## Pseudo-code realization:
![image](https://github.com/whskn/Universally-Fair-Scheduler-Visualization/assets/76423174/a1ea0ad2-faa9-48d3-9c58-59f208634541)

## How it works?
The scheduler SFAIR has the following intuitive interpretation.
- Every process p ∈ {1, . . . , n} is associated with a weight zp that is used by
SFAIR for determining the next process to be scheduled. The weights are
de ned in line 1. The weights can take values from Z, the set of integral
numbers.
- On initialisation (line 7), every weight zi is initialised by a non-negative
random value from N0 .
- In each scheduling cycle,
1. SFAIR inputs the set E of all runnable processes (line 10).
2.  Then it selects a process p to be scheduled next (line 11), such that p is one of the runnable processes with smallest weight. Since several processes may ful l this condition, a random selection is performed among them.
3. he weight zp of the process to be scheduled is set to a new random value from N0 (line 12).
