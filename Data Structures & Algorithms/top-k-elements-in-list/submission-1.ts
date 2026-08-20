class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const seen = new Map<number, number>();

        nums.forEach(n => {
            seen.set(n, (seen.get(n) ?? 0) + 1)
        })

        const sorted = Array.from(seen.entries())
            .sort(([_keyA, valueA], [_keyB, valueB]) => valueB - valueA)

        const result = [];

        for (let i = 0; i < k; i++) {
            const [key] = sorted[i];
            result.push(key);
        }

        return result;
    }
}
