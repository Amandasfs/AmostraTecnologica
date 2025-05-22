import { View, Image, ActivityIndicator, Text } from 'react-native';
import { useEffect } from 'react';
import { useNavigation } from '@react-navigation/native';
import styles from '../assets/styles/loadingStyles';

export default function Loading() {
  const navigation = useNavigation();

  useEffect(() => {
    const timeout = setTimeout(() => {
      navigation.replace('Login'); // Redireciona para Login
    }, 2000);

    return () => clearTimeout(timeout);
  }, []);

  return (
    <View style={styles.container}>
      <Image source={require('../assets/img/LogoSF.png')} style={styles.logo} />
      <ActivityIndicator size="large" color="#ff5900" />
      <Text style={styles.loadingText}>Carregando...</Text>
    </View>
  );
}
