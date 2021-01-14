import networkx as nx
import EoN
import matplotlib.pyplot as plt


def epidemy_without_recover(graph, initial_nodes, transmission_rate, plot_tittle='', return_full_data=False):




    if return_full_data:
        return EoN.fast_SIR(graph, transmission_rate, gamma=0,
                              initial_infecteds=initial_nodes, return_full_data=return_full_data)

    else:
        t, S, I, R = EoN.fast_SIR(graph, transmission_rate, gamma=0,
                                  initial_infecteds=initial_nodes)
        max_time_index = 0
        for i in range(0,len(I)):
            if I[i] > 0.9*graph.number_of_nodes():
                print(f'Infectados:{I[i]} = Limiar:{0.9*graph.number_of_nodes()}')
                max_time_index = i
                break


        t = t*100

        plt.plot(t, I, label=plot_tittle)
        #plt.plot(t, S, label='Suscetivel', color='b')

        #plt.hlines(I[max_time_index], t[0], t[max_time_index], colors='k')
        #plt.vlines(t[max_time_index], I[0], I[max_time_index], colors='k')




    #plt.xticks([t[max_time_index]])
    #plt.yticks([I[max_time_index]])

    plt.legend(loc='best')


def epidemy_with_recover(graph, initial_nodes, transmission_rate, recovery_rate, plot_tittle='', return_full_data=False):




    if return_full_data:
        return EoN.fast_SIR(graph, transmission_rate, gamma=recovery_rate,
                              initial_infecteds=initial_nodes, return_full_data=return_full_data)

    else:
        t, S, I, R = EoN.fast_SIR(graph, transmission_rate, gamma=recovery_rate,
                                  initial_infecteds=initial_nodes)
        max_time_index = 0
        biggest_number_infected = 0
        for i in range(0,len(I)):
            if I[i] > biggest_number_infected:
                print(f'Infectados:{I[i]} = Limiar:{biggest_number_infected}')
                biggest_number_infected = I[i]
                max_time_index = i


        t = t*100

        plt.title(plot_tittle)

        plt.plot(t, I, label='Infectados')
        plt.plot(t, S, label='Suscetivel')
        plt.plot(t, R, label='Removidos')

        plt.hlines(I[max_time_index], t[0], t[max_time_index], colors='k')
        plt.vlines(t[max_time_index], I[0], I[max_time_index], colors='k')

    plt.xlim(0, max(t))
    plt.ylim(0, graph.number_of_nodes())
    plt.xticks([t[max_time_index]])
    plt.yticks([I[max_time_index]])

    plt.legend(loc='best')
    plt.show()



