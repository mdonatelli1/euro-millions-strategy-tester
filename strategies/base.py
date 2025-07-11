from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    @abstractmethod
    def predict(self, history):
        """
        Retourne une prédiction (liste de numéros) à partir de l'historique.
        :param history: Liste des tirages précédents (chacun sous forme de liste ou tuple)
        :return: Tuple (liste de numéros principaux, liste d'étoiles)
        """
        pass

    def __str__(self):
        return self.__class__.__name__
