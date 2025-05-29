import React, { useState } from 'react';
import { View, Text, TextInput, Pressable, Animated, Image } from 'react-native';
import styles from '../assets/styles/loginStyles';
import { LoginScreenNavigationProp } from '../types/navigation'; // ajuste o caminho conforme necessário

type Props = {
  navigation: LoginScreenNavigationProp;
};

export default function Login({ navigation }: Props): React.JSX.Element {
  const [emailFocused, setEmailFocused] = useState(false);
  const [passwordFocused, setPasswordFocused] = useState(false);
  const scale = new Animated.Value(1);

  const animateButton = () => {
    Animated.sequence([
      Animated.timing(scale, { toValue: 0.95, duration: 100, useNativeDriver: true }),
      Animated.timing(scale, { toValue: 1, duration: 100, useNativeDriver: true }),
    ]).start(() => {
      navigation.replace('Home');
    });
  };
  return (
    <View style={styles.container}>
      <Image source={require('../assets/img/LogoSF.png')} style={styles.logo} />
      <Text style={styles.title}>Bem-vindo ao SaneApp</Text>
      <Text style={styles.subtitle}>faça seu login</Text>

      <Text style={styles.label}>Email/CPF</Text>
      <TextInput
        style={[styles.input, emailFocused && styles.inputFocused]}
        onFocus={() => setEmailFocused(true)}
        onBlur={() => setEmailFocused(false)}
        keyboardType="email-address"
        autoCapitalize="none"
      />

      <Text style={styles.label}>Senha</Text>
      <TextInput
        style={[styles.input, passwordFocused && styles.inputFocused]}
        onFocus={() => setPasswordFocused(true)}
        onBlur={() => setPasswordFocused(false)}
        secureTextEntry
      />

      <View style={{ width: '100%' }}>
        <Pressable onPress={() => console.log('Navegar para recuperação de senha')}>
          <Text style={styles.forgotPasswordLink}>Esqueceu a senha?</Text>
        </Pressable>
      </View>

      <Animated.View style={{ transform: [{ scale }] }}>
        <Pressable
          onPress={animateButton}
          style={({ pressed }) => [
            styles.button,
            pressed && { opacity: 0.8 },
          ]}
        >
          <Text style={styles.buttonText}>Entrar</Text>
        </Pressable>

        <Pressable onPress={() => console.log('Navegar para tela de cadastro')}>
          <Text style={styles.registerLink}>
            Não tem uma conta? <Text style={styles.registerBold}>Cadastre-se</Text>
          </Text>
        </Pressable>
      </Animated.View>
    </View>
  );
}
