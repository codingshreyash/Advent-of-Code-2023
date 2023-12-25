from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    conditions: list
    # conditions describes all rating intervals that would necessarily lead you to this node
    rules: list[tuple]
workflow_nodes = {'A': Node([], []), 'R': Node([], [])}

parts = []
with open('input.txt', 'r') as f:
    mode = 'workflows'
    for line in f.readlines():
        if not line.strip():
            mode = 'ratings'
            continue
        if mode == 'workflows':
            workflow, right = line.strip().split('{')
            node = Node(conditions=[], rules=[])
            for rule in right[:-1].split(','):
                if ':' not in rule:
                    node.rules.append((rule,))
                    break
                condition, child = rule.split(':')
                var = condition[0]
                symbol = condition[1]
                value = int(condition[2:])
                node.rules.append((var, symbol, value, child))
            workflow_nodes[workflow] = node
        elif mode == 'ratings':
            rating_table = {}
            for kv in line.strip()[1:-1].split(','):
                rating_table[kv[0]] = int(kv[2:])
            parts.append(rating_table)

root = workflow_nodes['in']
start_condition = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}

def range_intersection(r1, r2):
    left = max(r1[0], r2[0])
    right = min(r1[1], r2[1])
    if right < left:
        return None
    return left, right

def process_node(node, condition):
    node.conditions.append(condition)
    temp_condition = condition.copy()
    for rule in node.rules:
        if len(rule) == 1:
            child_node = workflow_nodes[rule[0]]
            process_node(child_node, temp_condition)
            continue
        var, symbol, value, child = rule
        interval = (1, value-1) if symbol == '<' else (value+1, 4000)
        child_temp_condition = temp_condition.copy()
        child_temp_condition[var] = range_intersection(child_temp_condition[var], interval)
        if child_temp_condition[var] is not None:
            child_node = workflow_nodes[child]
            process_node(child_node, child_temp_condition)
        inverted_interval = (value, 4000) if symbol == '<' else (1, value)
        temp_condition[var] = range_intersection(temp_condition[var], inverted_interval)
        if temp_condition[var] is None:
            break
process_node(root, start_condition)

# part 1
total1 = 0
for part in parts:
    for condition in workflow_nodes['A'].conditions:
        if all(condition[char][0] <= part[char] <= condition[char][1] for char in 'xmas'):
            total1 += sum(part.values())
            break
print('part1:', total1)

# part 2
total2 = 0
for condition in workflow_nodes['A'].conditions:
    product = 1
    for p1, p2 in condition.values():
        product *= (p2 - p1 + 1)
    total2 += product

print('part2:', total2)