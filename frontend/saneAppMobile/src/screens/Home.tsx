import React from 'react';
import { View, Text } from 'react-native';
import styles from '../assets/styles/homeStyles';

export default function Home() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bem-vindo à Home!</Text>
      <Text style={styles.subtitle}>Esta é a tela inicial após o login</Text>
    </View>
  );
}
