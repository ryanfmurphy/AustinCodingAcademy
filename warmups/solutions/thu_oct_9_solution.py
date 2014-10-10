def file2dicts():
    with open('orders.txt') as fh:
        raw_text = fh.read().strip() # strip is important to get rid of the last newline
        lines = raw_text.split('\n')
        names = lines[::3] # every 3rd line
        products = lines[1::3] # every 3rd line starting with the 2nd line
        costs = lines[2::3] # every 3rd line starting with the 3nd line
        results = []
        for i in range(len(names)):
            results.append({'name':names[i], 'product':products[i], 'cost':float(costs[i])})
        return results

def dicts2file(results):
    file_lines = []
    for result in results:
        file_lines.append(result['name'])
        file_lines.append(result['product'])
        file_lines.append(str(result['cost']))
    file_text = '\n'.join(file_lines)
    with open('orders.txt','w') as fh:
        fh.write(file_text)

