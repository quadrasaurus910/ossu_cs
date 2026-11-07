from powerset import genPowerset
import knapsack

def chooseBest(pset, maxWeight, getVal, getWeight): 
    bestVal = 0.0
    bestSet = None
    for items in pset: 
        itemsVal = 0.0
        itemsWeight = 0.0 
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)
def testBest(maxWeight = 20):
    items = knapsack.buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, knapsack.Item.getValue,
        knapsack.Item.getWeight)
    print('Total value of items taken is', val)
    for item in taken:
        print(item)
    print(f"items len: {len(items)}, pset len: {len(pset)}")

testBest(120)